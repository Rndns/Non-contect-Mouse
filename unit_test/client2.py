import argparse
import numpy as np
import sys
import gevent.ssl

#import csv
import numpy as np
from pytictoc import TicToc

import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException

def parse_model_http(model_metadata, model_config):
    """
    Check the configuration of a model to make sure it meets the
    requirements for an image classification network (as expected by
    this client)
    """
    if len(model_metadata['inputs']) != 1:
        raise Exception("expecting 1 input, got {}".format(
            len(model_metadata['inputs'])))

    if len(model_config['input']) != 1:
        raise Exception(
            "expecting 1 input in model configuration, got {}".format(
                len(model_config['input'])))

    input_metadata = model_metadata['inputs'][0]
    output_metadata = model_metadata['outputs']

    return (input_metadata['name'], output_metadata,
            model_config['max_batch_size'])

def getTestData(data_file, ):
    from sklearn.model_selection import train_test_split
    dataset = data_file #'model/keypoint_classifier/keypoint.csv':

    RANDOM_SEED = 42
    NUM_CLASSES = 4
    TIME_STEPS = 16
    DIMENSION = 2

    if data_file.split('/')[-1].split('.')[-2] == 'point_history':
        x_dataset = np.loadtxt(dataset, delimiter=',', dtype='float32', usecols=list(range(1, (TIME_STEPS * DIMENSION) + 1)))
    else:
        x_dataset = np.loadtxt(dataset, delimiter=',', dtype='float32', usecols=list(range(1, (21 * 2) + 1)))
    
    y_dataset = np.loadtxt(dataset, delimiter=',', dtype='int32', usecols=(0))

    X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, train_size=0.75, random_state=RANDOM_SEED)

    return X_train, X_test, y_train, y_test


def callModel(model_name, 
                        input_data,
                        model_metadata,
                        output_metadata,
                        headers=None,
                        request_compression_algorithm=None,
                        response_compression_algorithm=None):
    inputs = []

    for _, inputInfo in enumerate(model_metadata['inputs']):
        inputs.append(
            httpclient.InferInput( name=inputInfo['name'], shape=input_data.shape, datatype=inputInfo['datatype'] )
            )
    

    output_names = [ output['name'] for output in output_metadata ]
    outputs = []
    for output_name in output_names:
            outputs.append(
                httpclient.InferRequestedOutput(output_name,
                                                binary_data=False,
                                                class_count=0)
                )

    assert len(inputs) == 1
    #input_1 = np.array([[0.0, 0.0, 0.19063545150501673, 0.033444816053511704, 0.38127090301003347, 0.043478260869565216, 0.5217391304347826, 0.13043478260869565, 0.6421404682274248, 0.1939799331103679, 0.3076923076923077, 0.35451505016722407, 0.4013377926421405, 0.5518394648829431, 0.4682274247491639, 0.7023411371237458, 0.5250836120401338, 0.8327759197324415, 0.17725752508361203, 0.42474916387959866, 0.24749163879598662, 0.6588628762541806, 0.2976588628762542, 0.8327759197324415, 0.34448160535117056, 0.9966555183946488, 0.043478260869565216, 0.43478260869565216, 0.09364548494983277, 0.6722408026755853, 0.12709030100334448, 0.8461538461538461, 0.1605351170568562, 1.0, 0.0903010033444816, 0.4013377926421405, 0.09364548494983277, 0.5919732441471572, 0.09698996655518395, 0.7224080267558528, 0.10033444816053512, 0.8461538461538461]], dtype=np.float32)
    inputs[0].set_data_from_numpy( input_data )#, binary_data=False )

    results = triton_client.infer(
        model_name,
        inputs=inputs,
        outputs=outputs,
        query_params=None,
        headers=headers,
        request_compression_algorithm=request_compression_algorithm,
        response_compression_algorithm=response_compression_algorithm)

    return results.get_response()

def doInference(model_name, model_metadata, output_metadata, data_file):

    #X_train, X_test, y_train, y_test = getTestData(data_file)
    _, X_test, _, y_test = getTestData(data_file)

    t = TicToc()

    output_data = dict()
    output_data['y_test'] = y_test

    output = []
    for index in range(X_test.shape[0]):
        t.tic()

        input_data = X_test[index].reshape(1,-1)
        result =  callModel( model_name=model_name, input_data=input_data, model_metadata=model_metadata, output_metadata=output_metadata )

        res = result['outputs'][0]['data']
        
        output.append( np.argmax(res).tolist() )

        t.toc()

    output_data['X_predict'] = np.array(output, dtype=np.int32).flatten()#.tolist()
    return output_data


def doEvaluation(output_data):
    compData = output_data['X_predict'] - output_data['y_test']

    numOfNonZero = np.count_nonzero(compData)
    numOfTotal = len(compData)
    Accuracy = np.around( (numOfTotal-numOfNonZero)*100 / numOfTotal, 2 )
    print(f"Accurcy : {numOfNonZero}/{numOfTotal} ({Accuracy}%)")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v',
                        '--verbose',
                        action="store_true",
                        required=False,
                        default=False,
                        help='Enable verbose output')
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        required=False,
                        default='localhost:8000',
                        help='Inference server URL. Default is localhost:8000.')
    parser.add_argument(
        '--insecure',
        action="store_true",
        required=False,
        default=False,
        help=
        'Use no peer verification in SSL communications. Use with caution. Default is False.'
    )
    parser.add_argument(
        '-m', '--model',
        type=str,
        required=True,
        default=False,
        help=
        'Use no peer verification in SSL communications. Use with caution. Default is False.'
    )
    parser.add_argument(
        '-d', '--dataset',
        type=str,
        required=True,
        default=False,
        help=
        'Use no peer verification in SSL communications. Use with caution. Default is False.'
    )

    FLAGS = parser.parse_args()
    try:
        triton_client = httpclient.InferenceServerClient(
            url=FLAGS.url, verbose=FLAGS.verbose)
    except Exception as e:
        print("channel creation failed: " + str(e))
        sys.exit(1)

    model_name = FLAGS.model
    data_file = FLAGS.dataset

    try:
        model_metadata = triton_client.get_model_metadata( model_name=model_name, model_version="" )
    except InferenceServerException as e:
        print("failed to retrieve the metadata: " + str(e))
        sys.exit(1)

    try:
        model_config = triton_client.get_model_config( model_name=model_name, model_version="" )
    except InferenceServerException as e:
        print("failed to retrieve the config: " + str(e))
        sys.exit(1)

    _, output_metadata, _ = parse_model_http( model_metadata, model_config )

    output = doInference( model_name, model_metadata, output_metadata, data_file )
    doEvaluation( output )
    
    statistics = triton_client.get_inference_statistics(model_name=model_name,
                                                        headers=None)
    print(statistics)
    if len(statistics['model_stats']) != 1:
        print("FAILED: Inference Statistics")
        sys.exit(1)


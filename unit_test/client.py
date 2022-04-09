import argparse
import numpy as np
import sys
import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException


def test_infer(model_name,
               input_1,
               headers=None,
               request_compression_algorithm=None,
               response_compression_algorithm=None):
    inputs = []
    outputs = []
    inputs.append(httpclient.InferInput('input_1', [1, 42], 'FP32'))

    # Initialize the data
    inputs[0].set_data_from_numpy(input_1)

    outputs.append(httpclient.InferRequestedOutput('Identity', [1, 4], 'FP32'))  # binary_data=True))

    query_params = {'test_1': 1, 'test_2': 2}
    results = triton_client.infer(
        model_name,
        inputs,
        outputs=outputs,
        query_params=None,
        headers=headers,
        request_compression_algorithm=request_compression_algorithm,
        response_compression_algorithm=response_compression_algorithm)

    return results


def test_infer_no_outputs(model_name,
                          input1_data,
                          headers=None,
                          request_compression_algorithm=None,
                          response_compression_algorithm=None):
    inputs = []
    inputs.append(httpclient.InferInput('input_1', (-1, 42), "INT32"))

    # Initialize the data
    inputs[1].set_data_from_numpy(input1_data, binary_data=True)

    query_params = {'test_1': 1, 'test_2': 2}
    results = triton_client.infer(
        model_name,
        inputs,
        outputs=None,
        query_params=query_params,
        headers=headers,
        request_compression_algorithm=request_compression_algorithm,
        response_compression_algorithm=response_compression_algorithm)

    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v',
                        '--verbose',
                        action="store_true",
                        required=False,
                        default=False,
                        help='Enable verbose output'
                        )
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        required=False,
                        default='localhost:8000',
                        help='Inference server URL. Default is localhost:8000.'
                        )
    parser.add_argument('-H',
                        dest='http_headers',
                        metavar="HTTP_HEADER",
                        required=False,
                        action='append',
                        help='HTTP headers to add to inference server requests. ' +
                        'Format is -H"Header:Value".'
                        )
    parser.add_argument('--request-compression-algorithm',
                        type=str,
                        required=False,
                        default=None,
                        help=
                        'The compression algorithm to be used when sending request body to server. Default is None.'
                        )
    parser.add_argument('--response-compression-algorithm',
                        type=str,
                        required=False,
                        default=None,
                        help=
                        'The compression algorithm to be used when receiving response body from server. Default is None.'
                        )
    parser.add_argument('-m',
                        '--model',
                        type=str,
                        required=False,
                        default='keypoint_onnx',
                        help='choice the deeplearning model'
                        )

    FLAGS = parser.parse_args()
    try:
        triton_client = httpclient.InferenceServerClient(
            url=FLAGS.url, verbose=FLAGS.verbose)
    except Exception as e:
        print("channel creation failed: " + str(e))
        sys.exit(1)

    model_name = FLAGS.model

    input_1 = np.array([[0.0, 0.0, 0.19063545150501673, 0.033444816053511704, 0.38127090301003347, 0.043478260869565216, 0.5217391304347826, 0.13043478260869565, 0.6421404682274248, 0.1939799331103679, 0.3076923076923077, 0.35451505016722407, 0.4013377926421405, 0.5518394648829431, 0.4682274247491639, 0.7023411371237458, 0.5250836120401338, 0.8327759197324415, 0.17725752508361203, 0.42474916387959866, 0.24749163879598662, 0.6588628762541806, 0.2976588628762542, 0.8327759197324415, 0.34448160535117056, 0.9966555183946488, 0.043478260869565216, 0.43478260869565216, 0.09364548494983277, 0.6722408026755853, 0.12709030100334448, 0.8461538461538461, 0.1605351170568562, 1.0, 0.0903010033444816, 0.4013377926421405, 0.09364548494983277, 0.5919732441471572, 0.09698996655518395, 0.7224080267558528, 0.10033444816053512, 0.8461538461538461]], dtype=np.float32)

    if model_name == 'pointHistory_onnx':
        input_1 = np.full(shape=(1, 32), fill_value=0.0, dtype=np.float32)

    if FLAGS.http_headers is not None:
        headers_dict = {
            l.split(':')[0]: l.split(':')[1] for l in FLAGS.http_headers
        }
    else:
        headers_dict = None

    # Infer with requested Outputs
    results = test_infer(model_name, input_1, headers_dict,
                         FLAGS.request_compression_algorithm,
                         FLAGS.response_compression_algorithm)
    print(results.get_response())

    statistics = triton_client.get_inference_statistics(model_name=model_name,
                                                        headers=headers_dict)
    print(statistics)
    if len(statistics['model_stats']) != 1:
        print("FAILED: Inference Statistics")
        sys.exit(1)

    results = test_infer_no_outputs(model_name, input_1,
                                    headers_dict,
                                    FLAGS.request_compression_algorithm,
                                    FLAGS.response_compression_algorithm)
    print(results.get_response())

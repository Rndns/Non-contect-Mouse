# triton model_meta get
# inference code

import sys
import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException


class TritonClient():
    def __init__(self, url, model_name, verbose=False) -> None:
        self.url = url
        self.model_name = model_name

        try:
            self.triton_client = httpclient.InferenceServerClient( url=self.url, verbose=verbose )
        except Exception as e:
            print("channel creation failed: " + str(e))
            sys.exit(1)

        try:
            self.model_metadata = self.triton_client.get_model_metadata( model_name=self.model_name, model_version="" )
        except InferenceServerException as e:
            print("failed to retrieve the metadata: " + str(e))
            sys.exit(1)

        try:
            self.model_config = self.triton_client.get_model_config( model_name=self.model_name, model_version="" )
        except InferenceServerException as e:
            print("failed to retrieve the config: " + str(e))
            sys.exit(1)

        _, self.output_metadata, _ = self.parse_model_http( self.model_metadata, self.model_config )


    def callModel(self, input_data,
                        headers=None,
                        request_compression_algorithm=None,
                        response_compression_algorithm=None):
        inputs = []

        for _, inputInfo in enumerate(self.model_metadata['inputs']):
            inputs.append(
                httpclient.InferInput( name=inputInfo['name'], shape=input_data.shape, datatype=inputInfo['datatype'] )
                )
        

        output_names = [ output['name'] for output in self.output_metadata ]
        outputs = []
        for output_name in output_names:
                outputs.append(
                    httpclient.InferRequestedOutput(output_name,
                                                    binary_data=False,
                                                    class_count=0)
                    )

        assert len(inputs) == 1        
        inputs[0].set_data_from_numpy( input_data , binary_data=False )

        results = self.triton_client.infer(
            self.model_name,
            inputs=inputs,
            outputs=outputs,
            query_params=None,
            headers=headers,
            request_compression_algorithm=request_compression_algorithm,
            response_compression_algorithm=response_compression_algorithm)

        return results.get_response()

    def parse_model_http(self, model_metadata, model_config):
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
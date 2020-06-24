# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import info_pb2 as info_dot_info__pb2


class InfoServiceStub(object):
    """Provide information about the hardware and/or software of a system.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFlightInformation = channel.unary_unary(
                '/mavsdk.rpc.info.InfoService/GetFlightInformation',
                request_serializer=info_dot_info__pb2.GetFlightInformationRequest.SerializeToString,
                response_deserializer=info_dot_info__pb2.GetFlightInformationResponse.FromString,
                )
        self.GetIdentification = channel.unary_unary(
                '/mavsdk.rpc.info.InfoService/GetIdentification',
                request_serializer=info_dot_info__pb2.GetIdentificationRequest.SerializeToString,
                response_deserializer=info_dot_info__pb2.GetIdentificationResponse.FromString,
                )
        self.GetProduct = channel.unary_unary(
                '/mavsdk.rpc.info.InfoService/GetProduct',
                request_serializer=info_dot_info__pb2.GetProductRequest.SerializeToString,
                response_deserializer=info_dot_info__pb2.GetProductResponse.FromString,
                )
        self.GetVersion = channel.unary_unary(
                '/mavsdk.rpc.info.InfoService/GetVersion',
                request_serializer=info_dot_info__pb2.GetVersionRequest.SerializeToString,
                response_deserializer=info_dot_info__pb2.GetVersionResponse.FromString,
                )


class InfoServiceServicer(object):
    """Provide information about the hardware and/or software of a system.
    """

    def GetFlightInformation(self, request, context):
        """Get flight information of the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIdentification(self, request, context):
        """Get the identification of the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProduct(self, request, context):
        """Get product information of the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
        """Get the version information of the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InfoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFlightInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFlightInformation,
                    request_deserializer=info_dot_info__pb2.GetFlightInformationRequest.FromString,
                    response_serializer=info_dot_info__pb2.GetFlightInformationResponse.SerializeToString,
            ),
            'GetIdentification': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIdentification,
                    request_deserializer=info_dot_info__pb2.GetIdentificationRequest.FromString,
                    response_serializer=info_dot_info__pb2.GetIdentificationResponse.SerializeToString,
            ),
            'GetProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProduct,
                    request_deserializer=info_dot_info__pb2.GetProductRequest.FromString,
                    response_serializer=info_dot_info__pb2.GetProductResponse.SerializeToString,
            ),
            'GetVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVersion,
                    request_deserializer=info_dot_info__pb2.GetVersionRequest.FromString,
                    response_serializer=info_dot_info__pb2.GetVersionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.info.InfoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InfoService(object):
    """Provide information about the hardware and/or software of a system.
    """

    @staticmethod
    def GetFlightInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.info.InfoService/GetFlightInformation',
            info_dot_info__pb2.GetFlightInformationRequest.SerializeToString,
            info_dot_info__pb2.GetFlightInformationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIdentification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.info.InfoService/GetIdentification',
            info_dot_info__pb2.GetIdentificationRequest.SerializeToString,
            info_dot_info__pb2.GetIdentificationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.info.InfoService/GetProduct',
            info_dot_info__pb2.GetProductRequest.SerializeToString,
            info_dot_info__pb2.GetProductResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.info.InfoService/GetVersion',
            info_dot_info__pb2.GetVersionRequest.SerializeToString,
            info_dot_info__pb2.GetVersionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
    'get_certificate_output',
]

@pulumi.output_type
class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    def __init__(__self__, certificate=None, certificate_chain=None, id=None, name=None):
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        pulumi.set(__self__, "certificate", certificate)
        if certificate_chain and not isinstance(certificate_chain, str):
            raise TypeError("Expected argument 'certificate_chain' to be a str")
        pulumi.set(__self__, "certificate_chain", certificate_chain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def certificate(self) -> str:
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> str:
        return pulumi.get(self, "certificate_chain")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            certificate=self.certificate,
            certificate_chain=self.certificate_chain,
            id=self.id,
            name=self.name)


def get_certificate(certificate: Optional[str] = None,
                    certificate_chain: Optional[str] = None,
                    id: Optional[str] = None,
                    name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['certificate'] = certificate
    __args__['certificateChain'] = certificate_chain
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        certificate=pulumi.get(__ret__, 'certificate'),
        certificate_chain=pulumi.get(__ret__, 'certificate_chain'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))
def get_certificate_output(certificate: Optional[pulumi.Input[Optional[str]]] = None,
                           certificate_chain: Optional[pulumi.Input[Optional[str]]] = None,
                           id: Optional[pulumi.Input[Optional[str]]] = None,
                           name: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['certificate'] = certificate
    __args__['certificateChain'] = certificate_chain
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult)
    return __ret__.apply(lambda __response__: GetCertificateResult(
        certificate=pulumi.get(__response__, 'certificate'),
        certificate_chain=pulumi.get(__response__, 'certificate_chain'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name')))

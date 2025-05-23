# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
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
from .. import _utilities

__all__ = ['AutoCertificateArgs', 'AutoCertificate']

@pulumi.input_type
class AutoCertificateArgs:
    def __init__(__self__, *,
                 common_name: pulumi.Input[str],
                 key_algorithm: pulumi.Input[str],
                 location: pulumi.Input[str],
                 provider_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AutoCertificate resource.
        :param pulumi.Input[str] common_name: [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
        :param pulumi.Input[str] key_algorithm: [string] The key algorithm used to generate the certificate.
        :param pulumi.Input[str] location: [string] The location of the auto-certificate.
        :param pulumi.Input[str] provider_id: [string] The certificate provider used to issue the certificates.
        :param pulumi.Input[str] name: [string] A certificate name used for management purposes.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alternative_names: [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
        """
        pulumi.set(__self__, "common_name", common_name)
        pulumi.set(__self__, "key_algorithm", key_algorithm)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "provider_id", provider_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if subject_alternative_names is not None:
            pulumi.set(__self__, "subject_alternative_names", subject_alternative_names)

    @property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Input[str]:
        """
        [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
        """
        return pulumi.get(self, "common_name")

    @common_name.setter
    def common_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "common_name", value)

    @property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Input[str]:
        """
        [string] The key algorithm used to generate the certificate.
        """
        return pulumi.get(self, "key_algorithm")

    @key_algorithm.setter
    def key_algorithm(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_algorithm", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        [string] The location of the auto-certificate.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Input[str]:
        """
        [string] The certificate provider used to issue the certificates.
        """
        return pulumi.get(self, "provider_id")

    @provider_id.setter
    def provider_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A certificate name used for management purposes.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
        """
        return pulumi.get(self, "subject_alternative_names")

    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subject_alternative_names", value)


@pulumi.input_type
class _AutoCertificateState:
    def __init__(__self__, *,
                 common_name: Optional[pulumi.Input[str]] = None,
                 key_algorithm: Optional[pulumi.Input[str]] = None,
                 last_issued_certificate_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering AutoCertificate resources.
        :param pulumi.Input[str] common_name: [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
        :param pulumi.Input[str] key_algorithm: [string] The key algorithm used to generate the certificate.
        :param pulumi.Input[str] last_issued_certificate_id: [string] The ID of the last certificate that was issued.
        :param pulumi.Input[str] location: [string] The location of the auto-certificate.
        :param pulumi.Input[str] name: [string] A certificate name used for management purposes.
        :param pulumi.Input[str] provider_id: [string] The certificate provider used to issue the certificates.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alternative_names: [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
        """
        if common_name is not None:
            pulumi.set(__self__, "common_name", common_name)
        if key_algorithm is not None:
            pulumi.set(__self__, "key_algorithm", key_algorithm)
        if last_issued_certificate_id is not None:
            pulumi.set(__self__, "last_issued_certificate_id", last_issued_certificate_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provider_id is not None:
            pulumi.set(__self__, "provider_id", provider_id)
        if subject_alternative_names is not None:
            pulumi.set(__self__, "subject_alternative_names", subject_alternative_names)

    @property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
        """
        return pulumi.get(self, "common_name")

    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "common_name", value)

    @property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The key algorithm used to generate the certificate.
        """
        return pulumi.get(self, "key_algorithm")

    @key_algorithm.setter
    def key_algorithm(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_algorithm", value)

    @property
    @pulumi.getter(name="lastIssuedCertificateId")
    def last_issued_certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of the last certificate that was issued.
        """
        return pulumi.get(self, "last_issued_certificate_id")

    @last_issued_certificate_id.setter
    def last_issued_certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_issued_certificate_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the auto-certificate.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A certificate name used for management purposes.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The certificate provider used to issue the certificates.
        """
        return pulumi.get(self, "provider_id")

    @provider_id.setter
    def provider_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_id", value)

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
        """
        return pulumi.get(self, "subject_alternative_names")

    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subject_alternative_names", value)


class AutoCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 common_name: Optional[pulumi.Input[str]] = None,
                 key_algorithm: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a **CM AutoCertificate**.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.cert.AutoCertificateProvider("example",
            name="Let's Encrypt",
            email="user@example.com",
            location="de/fra",
            server="https://acme-v02.api.letsencrypt.org/directory",
            external_account_binding={
                "key_id": "some-key-id",
                "key_secret": "secret",
            })
        example_auto_certificate = ionoscloud.cert.AutoCertificate("example",
            provider_id=example.id,
            common_name="www.example.com",
            location=example.location,
            key_algorithm="rsa4096",
            name="My Auto renewed certificate",
            subject_alternative_names=["app.example.com"])
        ```

        ## Import

        The resource can be imported using the `auto_certificate_id` and the `location`, separated by `:`, e.g.

        ```sh
        $ pulumi import ionoscloud:cert/autoCertificate:AutoCertificate example location:auto_certificate_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] common_name: [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
        :param pulumi.Input[str] key_algorithm: [string] The key algorithm used to generate the certificate.
        :param pulumi.Input[str] location: [string] The location of the auto-certificate.
        :param pulumi.Input[str] name: [string] A certificate name used for management purposes.
        :param pulumi.Input[str] provider_id: [string] The certificate provider used to issue the certificates.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alternative_names: [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutoCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **CM AutoCertificate**.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.cert.AutoCertificateProvider("example",
            name="Let's Encrypt",
            email="user@example.com",
            location="de/fra",
            server="https://acme-v02.api.letsencrypt.org/directory",
            external_account_binding={
                "key_id": "some-key-id",
                "key_secret": "secret",
            })
        example_auto_certificate = ionoscloud.cert.AutoCertificate("example",
            provider_id=example.id,
            common_name="www.example.com",
            location=example.location,
            key_algorithm="rsa4096",
            name="My Auto renewed certificate",
            subject_alternative_names=["app.example.com"])
        ```

        ## Import

        The resource can be imported using the `auto_certificate_id` and the `location`, separated by `:`, e.g.

        ```sh
        $ pulumi import ionoscloud:cert/autoCertificate:AutoCertificate example location:auto_certificate_id
        ```

        :param str resource_name: The name of the resource.
        :param AutoCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutoCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 common_name: Optional[pulumi.Input[str]] = None,
                 key_algorithm: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_id: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AutoCertificateArgs.__new__(AutoCertificateArgs)

            if common_name is None and not opts.urn:
                raise TypeError("Missing required property 'common_name'")
            __props__.__dict__["common_name"] = common_name
            if key_algorithm is None and not opts.urn:
                raise TypeError("Missing required property 'key_algorithm'")
            __props__.__dict__["key_algorithm"] = key_algorithm
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if provider_id is None and not opts.urn:
                raise TypeError("Missing required property 'provider_id'")
            __props__.__dict__["provider_id"] = provider_id
            __props__.__dict__["subject_alternative_names"] = subject_alternative_names
            __props__.__dict__["last_issued_certificate_id"] = None
        super(AutoCertificate, __self__).__init__(
            'ionoscloud:cert/autoCertificate:AutoCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            common_name: Optional[pulumi.Input[str]] = None,
            key_algorithm: Optional[pulumi.Input[str]] = None,
            last_issued_certificate_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            provider_id: Optional[pulumi.Input[str]] = None,
            subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'AutoCertificate':
        """
        Get an existing AutoCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] common_name: [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
        :param pulumi.Input[str] key_algorithm: [string] The key algorithm used to generate the certificate.
        :param pulumi.Input[str] last_issued_certificate_id: [string] The ID of the last certificate that was issued.
        :param pulumi.Input[str] location: [string] The location of the auto-certificate.
        :param pulumi.Input[str] name: [string] A certificate name used for management purposes.
        :param pulumi.Input[str] provider_id: [string] The certificate provider used to issue the certificates.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subject_alternative_names: [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AutoCertificateState.__new__(_AutoCertificateState)

        __props__.__dict__["common_name"] = common_name
        __props__.__dict__["key_algorithm"] = key_algorithm
        __props__.__dict__["last_issued_certificate_id"] = last_issued_certificate_id
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["provider_id"] = provider_id
        __props__.__dict__["subject_alternative_names"] = subject_alternative_names
        return AutoCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Output[str]:
        """
        [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
        """
        return pulumi.get(self, "common_name")

    @property
    @pulumi.getter(name="keyAlgorithm")
    def key_algorithm(self) -> pulumi.Output[str]:
        """
        [string] The key algorithm used to generate the certificate.
        """
        return pulumi.get(self, "key_algorithm")

    @property
    @pulumi.getter(name="lastIssuedCertificateId")
    def last_issued_certificate_id(self) -> pulumi.Output[str]:
        """
        [string] The ID of the last certificate that was issued.
        """
        return pulumi.get(self, "last_issued_certificate_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [string] The location of the auto-certificate.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] A certificate name used for management purposes.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Output[str]:
        """
        [string] The certificate provider used to issue the certificates.
        """
        return pulumi.get(self, "provider_id")

    @property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
        """
        return pulumi.get(self, "subject_alternative_names")


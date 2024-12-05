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
from . import outputs
from ._inputs import *

__all__ = ['ContainerRegistryTokenArgs', 'ContainerRegistryToken']

@pulumi.input_type
class ContainerRegistryTokenArgs:
    def __init__(__self__, *,
                 registry_id: pulumi.Input[str],
                 expiry_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 save_password_to_file: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenScopeArgs']]]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ContainerRegistryToken resource.
        :param pulumi.Input[str] name: [string]
        :param pulumi.Input[str] save_password_to_file: [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
               
               > **⚠ WARNING** `save_password_to_file` must be used with caution.
               > It will save the password(token) returned on create to a file. This is the only way to get the token.
        :param pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenScopeArgs']]] scopes: [map]
        :param pulumi.Input[str] status: [string] Must have on of the values: `enabled`, `disabled`
        """
        pulumi.set(__self__, "registry_id", registry_id)
        if expiry_date is not None:
            pulumi.set(__self__, "expiry_date", expiry_date)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if save_password_to_file is not None:
            pulumi.set(__self__, "save_password_to_file", save_password_to_file)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_id", value)

    @property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expiry_date")

    @expiry_date.setter
    def expiry_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry_date", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string]
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="savePasswordToFile")
    def save_password_to_file(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path

        > **⚠ WARNING** `save_password_to_file` must be used with caution.
        > It will save the password(token) returned on create to a file. This is the only way to get the token.
        """
        return pulumi.get(self, "save_password_to_file")

    @save_password_to_file.setter
    def save_password_to_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "save_password_to_file", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenScopeArgs']]]]:
        """
        [map]
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenScopeArgs']]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Must have on of the values: `enabled`, `disabled`
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class _ContainerRegistryTokenState:
    def __init__(__self__, *,
                 credentials: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenCredentialArgs']]]] = None,
                 expiry_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 save_password_to_file: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenScopeArgs']]]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ContainerRegistryToken resources.
        :param pulumi.Input[str] name: [string]
        :param pulumi.Input[str] save_password_to_file: [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
               
               > **⚠ WARNING** `save_password_to_file` must be used with caution.
               > It will save the password(token) returned on create to a file. This is the only way to get the token.
        :param pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenScopeArgs']]] scopes: [map]
        :param pulumi.Input[str] status: [string] Must have on of the values: `enabled`, `disabled`
        """
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if expiry_date is not None:
            pulumi.set(__self__, "expiry_date", expiry_date)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if registry_id is not None:
            pulumi.set(__self__, "registry_id", registry_id)
        if save_password_to_file is not None:
            pulumi.set(__self__, "save_password_to_file", save_password_to_file)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenCredentialArgs']]]]:
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenCredentialArgs']]]]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expiry_date")

    @expiry_date.setter
    def expiry_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry_date", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string]
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "registry_id")

    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registry_id", value)

    @property
    @pulumi.getter(name="savePasswordToFile")
    def save_password_to_file(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path

        > **⚠ WARNING** `save_password_to_file` must be used with caution.
        > It will save the password(token) returned on create to a file. This is the only way to get the token.
        """
        return pulumi.get(self, "save_password_to_file")

    @save_password_to_file.setter
    def save_password_to_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "save_password_to_file", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenScopeArgs']]]]:
        """
        [map]
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryTokenScopeArgs']]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Must have on of the values: `enabled`, `disabled`
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class ContainerRegistryToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expiry_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 save_password_to_file: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryTokenScopeArgs', 'ContainerRegistryTokenScopeArgsDict']]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an **Container Registry Token** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_container_registry = ionoscloud.ContainerRegistry("exampleContainerRegistry",
            garbage_collection_schedule=ionoscloud.ContainerRegistryGarbageCollectionScheduleArgs(
                days=[
                    "Monday",
                    "Tuesday",
                ],
                time="05:19:00+00:00",
            ),
            location="de/fra")
        example_container_registry_token = ionoscloud.ContainerRegistryToken("exampleContainerRegistryToken",
            expiry_date="2023-01-13 16:27:42Z",
            scopes=[ionoscloud.ContainerRegistryTokenScopeArgs(
                actions=["push"],
                name="Scope1",
                type="repository",
            )],
            status="enabled",
            registry_id=example_container_registry.id,
            save_password_to_file="pass.txt")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Container Registry Token can be imported using the `container registry id` and `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/containerRegistryToken:ContainerRegistryToken mycrtoken {container_registry uuid}/{container_registry_token uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: [string]
        :param pulumi.Input[str] save_password_to_file: [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
               
               > **⚠ WARNING** `save_password_to_file` must be used with caution.
               > It will save the password(token) returned on create to a file. This is the only way to get the token.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryTokenScopeArgs', 'ContainerRegistryTokenScopeArgsDict']]]] scopes: [map]
        :param pulumi.Input[str] status: [string] Must have on of the values: `enabled`, `disabled`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerRegistryTokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an **Container Registry Token** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_container_registry = ionoscloud.ContainerRegistry("exampleContainerRegistry",
            garbage_collection_schedule=ionoscloud.ContainerRegistryGarbageCollectionScheduleArgs(
                days=[
                    "Monday",
                    "Tuesday",
                ],
                time="05:19:00+00:00",
            ),
            location="de/fra")
        example_container_registry_token = ionoscloud.ContainerRegistryToken("exampleContainerRegistryToken",
            expiry_date="2023-01-13 16:27:42Z",
            scopes=[ionoscloud.ContainerRegistryTokenScopeArgs(
                actions=["push"],
                name="Scope1",
                type="repository",
            )],
            status="enabled",
            registry_id=example_container_registry.id,
            save_password_to_file="pass.txt")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Container Registry Token can be imported using the `container registry id` and `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/containerRegistryToken:ContainerRegistryToken mycrtoken {container_registry uuid}/{container_registry_token uuid}
        ```

        :param str resource_name: The name of the resource.
        :param ContainerRegistryTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerRegistryTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expiry_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 registry_id: Optional[pulumi.Input[str]] = None,
                 save_password_to_file: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryTokenScopeArgs', 'ContainerRegistryTokenScopeArgsDict']]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerRegistryTokenArgs.__new__(ContainerRegistryTokenArgs)

            __props__.__dict__["expiry_date"] = expiry_date
            __props__.__dict__["name"] = name
            if registry_id is None and not opts.urn:
                raise TypeError("Missing required property 'registry_id'")
            __props__.__dict__["registry_id"] = registry_id
            __props__.__dict__["save_password_to_file"] = save_password_to_file
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["status"] = status
            __props__.__dict__["credentials"] = None
        super(ContainerRegistryToken, __self__).__init__(
            'ionoscloud:index/containerRegistryToken:ContainerRegistryToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            credentials: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryTokenCredentialArgs', 'ContainerRegistryTokenCredentialArgsDict']]]]] = None,
            expiry_date: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            registry_id: Optional[pulumi.Input[str]] = None,
            save_password_to_file: Optional[pulumi.Input[str]] = None,
            scopes: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryTokenScopeArgs', 'ContainerRegistryTokenScopeArgsDict']]]]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'ContainerRegistryToken':
        """
        Get an existing ContainerRegistryToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: [string]
        :param pulumi.Input[str] save_password_to_file: [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
               
               > **⚠ WARNING** `save_password_to_file` must be used with caution.
               > It will save the password(token) returned on create to a file. This is the only way to get the token.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryTokenScopeArgs', 'ContainerRegistryTokenScopeArgsDict']]]] scopes: [map]
        :param pulumi.Input[str] status: [string] Must have on of the values: `enabled`, `disabled`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ContainerRegistryTokenState.__new__(_ContainerRegistryTokenState)

        __props__.__dict__["credentials"] = credentials
        __props__.__dict__["expiry_date"] = expiry_date
        __props__.__dict__["name"] = name
        __props__.__dict__["registry_id"] = registry_id
        __props__.__dict__["save_password_to_file"] = save_password_to_file
        __props__.__dict__["scopes"] = scopes
        __props__.__dict__["status"] = status
        return ContainerRegistryToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Sequence['outputs.ContainerRegistryTokenCredential']]:
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "expiry_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string]
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "registry_id")

    @property
    @pulumi.getter(name="savePasswordToFile")
    def save_password_to_file(self) -> pulumi.Output[Optional[str]]:
        """
        [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path

        > **⚠ WARNING** `save_password_to_file` must be used with caution.
        > It will save the password(token) returned on create to a file. This is the only way to get the token.
        """
        return pulumi.get(self, "save_password_to_file")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence['outputs.ContainerRegistryTokenScope']]:
        """
        [map]
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        [string] Must have on of the values: `enabled`, `disabled`
        """
        return pulumi.get(self, "status")


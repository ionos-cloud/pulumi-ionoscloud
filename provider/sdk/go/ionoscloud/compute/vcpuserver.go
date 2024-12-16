// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// Resource VCPU Server can be imported using the `resource id` and the `datacenter id`, for example, passing only resource id and datacenter id means that the first nic found linked to the server will be attached to it.
//
// ```sh
// $ pulumi import ionoscloud:compute/vCPUServer:VCPUServer myserver {datacenter uuid}/{server uuid}
// ```
//
// Optionally, you can pass `primary_nic` and `firewallrule_id` so terraform will know to import also the first nic and firewall rule (if it exists on the server):
//
// ```sh
// $ pulumi import ionoscloud:compute/vCPUServer:VCPUServer myserver {datacenter uuid}/{server uuid}/{primary nic id}/{firewall rule id}
// ```
type VCPUServer struct {
	pulumi.CustomResourceState

	// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
	AvailabilityZone pulumi.StringOutput `pulumi:"availabilityZone"`
	// ***DEPRECATED*** Please refer to compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the getImage data source.
	//
	// Deprecated: Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
	BootCdrom pulumi.StringOutput `pulumi:"bootCdrom"`
	// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
	BootImage pulumi.StringOutput `pulumi:"bootImage"`
	// The associated boot volume.
	BootVolume pulumi.StringOutput `pulumi:"bootVolume"`
	// [integer] Number of server CPU cores.
	Cores     pulumi.IntOutput    `pulumi:"cores"`
	CpuFamily pulumi.StringOutput `pulumi:"cpuFamily"`
	// [string] The ID of a Virtual Data Center.
	DatacenterId pulumi.StringOutput `pulumi:"datacenterId"`
	// The associated firewall rule.
	FirewallruleId pulumi.StringOutput `pulumi:"firewallruleId"`
	// The associated firewall rules.
	FirewallruleIds pulumi.StringArrayOutput `pulumi:"firewallruleIds"`
	// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
	ImageName pulumi.StringOutput `pulumi:"imageName"`
	// [string] The password for the image.
	ImagePassword pulumi.StringOutput `pulumi:"imagePassword"`
	// A list with the IDs for the volumes that are defined inside the server resource.
	//
	// > **⚠ WARNING**
	// >
	// > sshKeys field is immutable.
	InlineVolumeIds pulumi.StringArrayOutput `pulumi:"inlineVolumeIds"`
	// A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
	Labels VCPUServerLabelArrayOutput `pulumi:"labels"`
	// [string] The name of the server.
	Name pulumi.StringOutput `pulumi:"name"`
	// See the Nic section.
	Nic VCPUServerNicPtrOutput `pulumi:"nic"`
	// The associated IP address.
	PrimaryIp pulumi.StringOutput `pulumi:"primaryIp"`
	// The associated NIC.
	PrimaryNic pulumi.StringOutput `pulumi:"primaryNic"`
	// [integer] The amount of memory for the server in MB.
	Ram pulumi.IntOutput `pulumi:"ram"`
	// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
	SshKeys pulumi.StringArrayOutput `pulumi:"sshKeys"`
	Type    pulumi.StringOutput      `pulumi:"type"`
	// Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
	VmState pulumi.StringOutput `pulumi:"vmState"`
	// See the Volume section.
	Volume VCPUServerVolumeOutput `pulumi:"volume"`
}

// NewVCPUServer registers a new resource with the given unique name, arguments, and options.
func NewVCPUServer(ctx *pulumi.Context,
	name string, args *VCPUServerArgs, opts ...pulumi.ResourceOption) (*VCPUServer, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Cores == nil {
		return nil, errors.New("invalid value for required argument 'Cores'")
	}
	if args.DatacenterId == nil {
		return nil, errors.New("invalid value for required argument 'DatacenterId'")
	}
	if args.Ram == nil {
		return nil, errors.New("invalid value for required argument 'Ram'")
	}
	if args.Volume == nil {
		return nil, errors.New("invalid value for required argument 'Volume'")
	}
	if args.ImagePassword != nil {
		args.ImagePassword = pulumi.ToSecret(args.ImagePassword).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"imagePassword",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VCPUServer
	err := ctx.RegisterResource("ionoscloud:compute/vCPUServer:VCPUServer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVCPUServer gets an existing VCPUServer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVCPUServer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VCPUServerState, opts ...pulumi.ResourceOption) (*VCPUServer, error) {
	var resource VCPUServer
	err := ctx.ReadResource("ionoscloud:compute/vCPUServer:VCPUServer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VCPUServer resources.
type vcpuserverState struct {
	// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// ***DEPRECATED*** Please refer to compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the getImage data source.
	//
	// Deprecated: Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
	BootCdrom *string `pulumi:"bootCdrom"`
	// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
	BootImage *string `pulumi:"bootImage"`
	// The associated boot volume.
	BootVolume *string `pulumi:"bootVolume"`
	// [integer] Number of server CPU cores.
	Cores     *int    `pulumi:"cores"`
	CpuFamily *string `pulumi:"cpuFamily"`
	// [string] The ID of a Virtual Data Center.
	DatacenterId *string `pulumi:"datacenterId"`
	// The associated firewall rule.
	FirewallruleId *string `pulumi:"firewallruleId"`
	// The associated firewall rules.
	FirewallruleIds []string `pulumi:"firewallruleIds"`
	// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
	ImageName *string `pulumi:"imageName"`
	// [string] The password for the image.
	ImagePassword *string `pulumi:"imagePassword"`
	// A list with the IDs for the volumes that are defined inside the server resource.
	//
	// > **⚠ WARNING**
	// >
	// > sshKeys field is immutable.
	InlineVolumeIds []string `pulumi:"inlineVolumeIds"`
	// A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
	Labels []VCPUServerLabel `pulumi:"labels"`
	// [string] The name of the server.
	Name *string `pulumi:"name"`
	// See the Nic section.
	Nic *VCPUServerNic `pulumi:"nic"`
	// The associated IP address.
	PrimaryIp *string `pulumi:"primaryIp"`
	// The associated NIC.
	PrimaryNic *string `pulumi:"primaryNic"`
	// [integer] The amount of memory for the server in MB.
	Ram *int `pulumi:"ram"`
	// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
	SshKeys []string `pulumi:"sshKeys"`
	Type    *string  `pulumi:"type"`
	// Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
	VmState *string `pulumi:"vmState"`
	// See the Volume section.
	Volume *VCPUServerVolume `pulumi:"volume"`
}

type VCPUServerState struct {
	// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
	AvailabilityZone pulumi.StringPtrInput
	// ***DEPRECATED*** Please refer to compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the getImage data source.
	//
	// Deprecated: Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
	BootCdrom pulumi.StringPtrInput
	// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
	BootImage pulumi.StringPtrInput
	// The associated boot volume.
	BootVolume pulumi.StringPtrInput
	// [integer] Number of server CPU cores.
	Cores     pulumi.IntPtrInput
	CpuFamily pulumi.StringPtrInput
	// [string] The ID of a Virtual Data Center.
	DatacenterId pulumi.StringPtrInput
	// The associated firewall rule.
	FirewallruleId pulumi.StringPtrInput
	// The associated firewall rules.
	FirewallruleIds pulumi.StringArrayInput
	// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
	ImageName pulumi.StringPtrInput
	// [string] The password for the image.
	ImagePassword pulumi.StringPtrInput
	// A list with the IDs for the volumes that are defined inside the server resource.
	//
	// > **⚠ WARNING**
	// >
	// > sshKeys field is immutable.
	InlineVolumeIds pulumi.StringArrayInput
	// A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
	Labels VCPUServerLabelArrayInput
	// [string] The name of the server.
	Name pulumi.StringPtrInput
	// See the Nic section.
	Nic VCPUServerNicPtrInput
	// The associated IP address.
	PrimaryIp pulumi.StringPtrInput
	// The associated NIC.
	PrimaryNic pulumi.StringPtrInput
	// [integer] The amount of memory for the server in MB.
	Ram pulumi.IntPtrInput
	// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
	SshKeys pulumi.StringArrayInput
	Type    pulumi.StringPtrInput
	// Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
	VmState pulumi.StringPtrInput
	// See the Volume section.
	Volume VCPUServerVolumePtrInput
}

func (VCPUServerState) ElementType() reflect.Type {
	return reflect.TypeOf((*vcpuserverState)(nil)).Elem()
}

type vcpuserverArgs struct {
	// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// ***DEPRECATED*** Please refer to compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the getImage data source.
	//
	// Deprecated: Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
	BootCdrom *string `pulumi:"bootCdrom"`
	// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
	BootImage *string `pulumi:"bootImage"`
	// [integer] Number of server CPU cores.
	Cores int `pulumi:"cores"`
	// [string] The ID of a Virtual Data Center.
	DatacenterId string `pulumi:"datacenterId"`
	// The associated firewall rules.
	FirewallruleIds []string `pulumi:"firewallruleIds"`
	// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
	ImageName *string `pulumi:"imageName"`
	// [string] The password for the image.
	ImagePassword *string `pulumi:"imagePassword"`
	// A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
	Labels []VCPUServerLabel `pulumi:"labels"`
	// [string] The name of the server.
	Name *string `pulumi:"name"`
	// See the Nic section.
	Nic *VCPUServerNic `pulumi:"nic"`
	// [integer] The amount of memory for the server in MB.
	Ram int `pulumi:"ram"`
	// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
	SshKeys []string `pulumi:"sshKeys"`
	// Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
	VmState *string `pulumi:"vmState"`
	// See the Volume section.
	Volume VCPUServerVolume `pulumi:"volume"`
}

// The set of arguments for constructing a VCPUServer resource.
type VCPUServerArgs struct {
	// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
	AvailabilityZone pulumi.StringPtrInput
	// ***DEPRECATED*** Please refer to compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the getImage data source.
	//
	// Deprecated: Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
	BootCdrom pulumi.StringPtrInput
	// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
	BootImage pulumi.StringPtrInput
	// [integer] Number of server CPU cores.
	Cores pulumi.IntInput
	// [string] The ID of a Virtual Data Center.
	DatacenterId pulumi.StringInput
	// The associated firewall rules.
	FirewallruleIds pulumi.StringArrayInput
	// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
	ImageName pulumi.StringPtrInput
	// [string] The password for the image.
	ImagePassword pulumi.StringPtrInput
	// A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
	Labels VCPUServerLabelArrayInput
	// [string] The name of the server.
	Name pulumi.StringPtrInput
	// See the Nic section.
	Nic VCPUServerNicPtrInput
	// [integer] The amount of memory for the server in MB.
	Ram pulumi.IntInput
	// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
	SshKeys pulumi.StringArrayInput
	// Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
	VmState pulumi.StringPtrInput
	// See the Volume section.
	Volume VCPUServerVolumeInput
}

func (VCPUServerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vcpuserverArgs)(nil)).Elem()
}

type VCPUServerInput interface {
	pulumi.Input

	ToVCPUServerOutput() VCPUServerOutput
	ToVCPUServerOutputWithContext(ctx context.Context) VCPUServerOutput
}

func (*VCPUServer) ElementType() reflect.Type {
	return reflect.TypeOf((**VCPUServer)(nil)).Elem()
}

func (i *VCPUServer) ToVCPUServerOutput() VCPUServerOutput {
	return i.ToVCPUServerOutputWithContext(context.Background())
}

func (i *VCPUServer) ToVCPUServerOutputWithContext(ctx context.Context) VCPUServerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VCPUServerOutput)
}

// VCPUServerArrayInput is an input type that accepts VCPUServerArray and VCPUServerArrayOutput values.
// You can construct a concrete instance of `VCPUServerArrayInput` via:
//
//	VCPUServerArray{ VCPUServerArgs{...} }
type VCPUServerArrayInput interface {
	pulumi.Input

	ToVCPUServerArrayOutput() VCPUServerArrayOutput
	ToVCPUServerArrayOutputWithContext(context.Context) VCPUServerArrayOutput
}

type VCPUServerArray []VCPUServerInput

func (VCPUServerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VCPUServer)(nil)).Elem()
}

func (i VCPUServerArray) ToVCPUServerArrayOutput() VCPUServerArrayOutput {
	return i.ToVCPUServerArrayOutputWithContext(context.Background())
}

func (i VCPUServerArray) ToVCPUServerArrayOutputWithContext(ctx context.Context) VCPUServerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VCPUServerArrayOutput)
}

// VCPUServerMapInput is an input type that accepts VCPUServerMap and VCPUServerMapOutput values.
// You can construct a concrete instance of `VCPUServerMapInput` via:
//
//	VCPUServerMap{ "key": VCPUServerArgs{...} }
type VCPUServerMapInput interface {
	pulumi.Input

	ToVCPUServerMapOutput() VCPUServerMapOutput
	ToVCPUServerMapOutputWithContext(context.Context) VCPUServerMapOutput
}

type VCPUServerMap map[string]VCPUServerInput

func (VCPUServerMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VCPUServer)(nil)).Elem()
}

func (i VCPUServerMap) ToVCPUServerMapOutput() VCPUServerMapOutput {
	return i.ToVCPUServerMapOutputWithContext(context.Background())
}

func (i VCPUServerMap) ToVCPUServerMapOutputWithContext(ctx context.Context) VCPUServerMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VCPUServerMapOutput)
}

type VCPUServerOutput struct{ *pulumi.OutputState }

func (VCPUServerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VCPUServer)(nil)).Elem()
}

func (o VCPUServerOutput) ToVCPUServerOutput() VCPUServerOutput {
	return o
}

func (o VCPUServerOutput) ToVCPUServerOutputWithContext(ctx context.Context) VCPUServerOutput {
	return o
}

// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
func (o VCPUServerOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.AvailabilityZone }).(pulumi.StringOutput)
}

// ***DEPRECATED*** Please refer to compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the getImage data source.
//
// Deprecated: Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
func (o VCPUServerOutput) BootCdrom() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.BootCdrom }).(pulumi.StringOutput)
}

// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
func (o VCPUServerOutput) BootImage() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.BootImage }).(pulumi.StringOutput)
}

// The associated boot volume.
func (o VCPUServerOutput) BootVolume() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.BootVolume }).(pulumi.StringOutput)
}

// [integer] Number of server CPU cores.
func (o VCPUServerOutput) Cores() pulumi.IntOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.IntOutput { return v.Cores }).(pulumi.IntOutput)
}

func (o VCPUServerOutput) CpuFamily() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.CpuFamily }).(pulumi.StringOutput)
}

// [string] The ID of a Virtual Data Center.
func (o VCPUServerOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.DatacenterId }).(pulumi.StringOutput)
}

// The associated firewall rule.
func (o VCPUServerOutput) FirewallruleId() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.FirewallruleId }).(pulumi.StringOutput)
}

// The associated firewall rules.
func (o VCPUServerOutput) FirewallruleIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringArrayOutput { return v.FirewallruleIds }).(pulumi.StringArrayOutput)
}

// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
func (o VCPUServerOutput) ImageName() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.ImageName }).(pulumi.StringOutput)
}

// [string] The password for the image.
func (o VCPUServerOutput) ImagePassword() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.ImagePassword }).(pulumi.StringOutput)
}

// A list with the IDs for the volumes that are defined inside the server resource.
//
// > **⚠ WARNING**
// >
// > sshKeys field is immutable.
func (o VCPUServerOutput) InlineVolumeIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringArrayOutput { return v.InlineVolumeIds }).(pulumi.StringArrayOutput)
}

// A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
func (o VCPUServerOutput) Labels() VCPUServerLabelArrayOutput {
	return o.ApplyT(func(v *VCPUServer) VCPUServerLabelArrayOutput { return v.Labels }).(VCPUServerLabelArrayOutput)
}

// [string] The name of the server.
func (o VCPUServerOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// See the Nic section.
func (o VCPUServerOutput) Nic() VCPUServerNicPtrOutput {
	return o.ApplyT(func(v *VCPUServer) VCPUServerNicPtrOutput { return v.Nic }).(VCPUServerNicPtrOutput)
}

// The associated IP address.
func (o VCPUServerOutput) PrimaryIp() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.PrimaryIp }).(pulumi.StringOutput)
}

// The associated NIC.
func (o VCPUServerOutput) PrimaryNic() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.PrimaryNic }).(pulumi.StringOutput)
}

// [integer] The amount of memory for the server in MB.
func (o VCPUServerOutput) Ram() pulumi.IntOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.IntOutput { return v.Ram }).(pulumi.IntOutput)
}

// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
func (o VCPUServerOutput) SshKeys() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringArrayOutput { return v.SshKeys }).(pulumi.StringArrayOutput)
}

func (o VCPUServerOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
func (o VCPUServerOutput) VmState() pulumi.StringOutput {
	return o.ApplyT(func(v *VCPUServer) pulumi.StringOutput { return v.VmState }).(pulumi.StringOutput)
}

// See the Volume section.
func (o VCPUServerOutput) Volume() VCPUServerVolumeOutput {
	return o.ApplyT(func(v *VCPUServer) VCPUServerVolumeOutput { return v.Volume }).(VCPUServerVolumeOutput)
}

type VCPUServerArrayOutput struct{ *pulumi.OutputState }

func (VCPUServerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VCPUServer)(nil)).Elem()
}

func (o VCPUServerArrayOutput) ToVCPUServerArrayOutput() VCPUServerArrayOutput {
	return o
}

func (o VCPUServerArrayOutput) ToVCPUServerArrayOutputWithContext(ctx context.Context) VCPUServerArrayOutput {
	return o
}

func (o VCPUServerArrayOutput) Index(i pulumi.IntInput) VCPUServerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *VCPUServer {
		return vs[0].([]*VCPUServer)[vs[1].(int)]
	}).(VCPUServerOutput)
}

type VCPUServerMapOutput struct{ *pulumi.OutputState }

func (VCPUServerMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VCPUServer)(nil)).Elem()
}

func (o VCPUServerMapOutput) ToVCPUServerMapOutput() VCPUServerMapOutput {
	return o
}

func (o VCPUServerMapOutput) ToVCPUServerMapOutputWithContext(ctx context.Context) VCPUServerMapOutput {
	return o
}

func (o VCPUServerMapOutput) MapIndex(k pulumi.StringInput) VCPUServerOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *VCPUServer {
		return vs[0].(map[string]*VCPUServer)[vs[1].(string)]
	}).(VCPUServerOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VCPUServerInput)(nil)).Elem(), &VCPUServer{})
	pulumi.RegisterInputType(reflect.TypeOf((*VCPUServerArrayInput)(nil)).Elem(), VCPUServerArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VCPUServerMapInput)(nil)).Elem(), VCPUServerMap{})
	pulumi.RegisterOutputType(VCPUServerOutput{})
	pulumi.RegisterOutputType(VCPUServerArrayOutput{})
	pulumi.RegisterOutputType(VCPUServerMapOutput{})
}

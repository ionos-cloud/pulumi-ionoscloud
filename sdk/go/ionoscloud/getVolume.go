// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The volume data source can be used to search for and return existing volumes.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
func GetVolume(ctx *pulumi.Context, args *GetVolumeArgs, opts ...pulumi.InvokeOption) (*GetVolumeResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetVolumeResult
	err := ctx.Invoke("ionoscloud:index/getVolume:getVolume", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVolume.
type GetVolumeArgs struct {
	DatacenterId string `pulumi:"datacenterId"`
	// ID of the volume you want to search for.
	//
	// Either `volume` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// Name of an existing volume that you want to search for.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getVolume.
type GetVolumeResult struct {
	// The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable.
	AvailabilityZone string `pulumi:"availabilityZone"`
	// The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
	BackupUnitId string `pulumi:"backupUnitId"`
	// The UUID of the attached server.
	BootServer string `pulumi:"bootServer"`
	// The bus type of the volume: VIRTIO or IDE.
	Bus string `pulumi:"bus"`
	// Is capable of CPU hot plug (no reboot required)
	CpuHotPlug   bool   `pulumi:"cpuHotPlug"`
	DatacenterId string `pulumi:"datacenterId"`
	// The LUN ID of the storage volume. Null for volumes not mounted to any VM
	DeviceNumber int `pulumi:"deviceNumber"`
	// Is capable of Virt-IO drive hot plug (no reboot required)
	DiscVirtioHotPlug bool `pulumi:"discVirtioHotPlug"`
	// Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
	DiscVirtioHotUnplug bool `pulumi:"discVirtioHotUnplug"`
	// The volume type: HDD or SSD.
	DiskType string `pulumi:"diskType"`
	// The id of the volume.
	Id *string `pulumi:"id"`
	// The image or snapshot UUID.
	Image string `pulumi:"image"`
	// Required if `sshkeyPath` is not provided.
	ImagePassword string `pulumi:"imagePassword"`
	// The type of the licence.
	LicenceType string `pulumi:"licenceType"`
	// The name of the volume.
	Name *string `pulumi:"name"`
	// Is capable of nic hot plug (no reboot required)
	NicHotPlug bool `pulumi:"nicHotPlug"`
	// Is capable of nic hot unplug (no reboot required)
	NicHotUnplug bool `pulumi:"nicHotUnplug"`
	// Is capable of memory hot plug (no reboot required)
	RamHotPlug bool `pulumi:"ramHotPlug"`
	// The size of the volume in GB.
	Size int `pulumi:"size"`
	// The associated public SSH key.
	Sshkey string `pulumi:"sshkey"`
	// The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
	UserData string `pulumi:"userData"`
}

func GetVolumeOutput(ctx *pulumi.Context, args GetVolumeOutputArgs, opts ...pulumi.InvokeOption) GetVolumeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetVolumeResult, error) {
			args := v.(GetVolumeArgs)
			r, err := GetVolume(ctx, &args, opts...)
			var s GetVolumeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetVolumeResultOutput)
}

// A collection of arguments for invoking getVolume.
type GetVolumeOutputArgs struct {
	DatacenterId pulumi.StringInput `pulumi:"datacenterId"`
	// ID of the volume you want to search for.
	//
	// Either `volume` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing volume that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (GetVolumeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVolumeArgs)(nil)).Elem()
}

// A collection of values returned by getVolume.
type GetVolumeResultOutput struct{ *pulumi.OutputState }

func (GetVolumeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVolumeResult)(nil)).Elem()
}

func (o GetVolumeResultOutput) ToGetVolumeResultOutput() GetVolumeResultOutput {
	return o
}

func (o GetVolumeResultOutput) ToGetVolumeResultOutputWithContext(ctx context.Context) GetVolumeResultOutput {
	return o
}

// The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable.
func (o GetVolumeResultOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.AvailabilityZone }).(pulumi.StringOutput)
}

// The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
func (o GetVolumeResultOutput) BackupUnitId() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.BackupUnitId }).(pulumi.StringOutput)
}

// The UUID of the attached server.
func (o GetVolumeResultOutput) BootServer() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.BootServer }).(pulumi.StringOutput)
}

// The bus type of the volume: VIRTIO or IDE.
func (o GetVolumeResultOutput) Bus() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.Bus }).(pulumi.StringOutput)
}

// Is capable of CPU hot plug (no reboot required)
func (o GetVolumeResultOutput) CpuHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetVolumeResult) bool { return v.CpuHotPlug }).(pulumi.BoolOutput)
}

func (o GetVolumeResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// The LUN ID of the storage volume. Null for volumes not mounted to any VM
func (o GetVolumeResultOutput) DeviceNumber() pulumi.IntOutput {
	return o.ApplyT(func(v GetVolumeResult) int { return v.DeviceNumber }).(pulumi.IntOutput)
}

// Is capable of Virt-IO drive hot plug (no reboot required)
func (o GetVolumeResultOutput) DiscVirtioHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetVolumeResult) bool { return v.DiscVirtioHotPlug }).(pulumi.BoolOutput)
}

// Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
func (o GetVolumeResultOutput) DiscVirtioHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetVolumeResult) bool { return v.DiscVirtioHotUnplug }).(pulumi.BoolOutput)
}

// The volume type: HDD or SSD.
func (o GetVolumeResultOutput) DiskType() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.DiskType }).(pulumi.StringOutput)
}

// The id of the volume.
func (o GetVolumeResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetVolumeResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The image or snapshot UUID.
func (o GetVolumeResultOutput) Image() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.Image }).(pulumi.StringOutput)
}

// Required if `sshkeyPath` is not provided.
func (o GetVolumeResultOutput) ImagePassword() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.ImagePassword }).(pulumi.StringOutput)
}

// The type of the licence.
func (o GetVolumeResultOutput) LicenceType() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.LicenceType }).(pulumi.StringOutput)
}

// The name of the volume.
func (o GetVolumeResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetVolumeResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// Is capable of nic hot plug (no reboot required)
func (o GetVolumeResultOutput) NicHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetVolumeResult) bool { return v.NicHotPlug }).(pulumi.BoolOutput)
}

// Is capable of nic hot unplug (no reboot required)
func (o GetVolumeResultOutput) NicHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetVolumeResult) bool { return v.NicHotUnplug }).(pulumi.BoolOutput)
}

// Is capable of memory hot plug (no reboot required)
func (o GetVolumeResultOutput) RamHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetVolumeResult) bool { return v.RamHotPlug }).(pulumi.BoolOutput)
}

// The size of the volume in GB.
func (o GetVolumeResultOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v GetVolumeResult) int { return v.Size }).(pulumi.IntOutput)
}

// The associated public SSH key.
func (o GetVolumeResultOutput) Sshkey() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.Sshkey }).(pulumi.StringOutput)
}

// The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
func (o GetVolumeResultOutput) UserData() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumeResult) string { return v.UserData }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetVolumeResultOutput{})
}

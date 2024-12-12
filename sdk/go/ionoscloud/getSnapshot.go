// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Snapshot data source** can be used to search for and return an existing snapshot which can then be used to provision a server. If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By Name & Size & Location
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := ionoscloud.GetSnapshot(ctx, &ionoscloud.GetSnapshotArgs{
//				Location: pulumi.StringRef("us/las"),
//				Name:     pulumi.StringRef("Snapshot Example"),
//				Size:     pulumi.IntRef(2),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
// Note: The size argument is in GB
func GetSnapshot(ctx *pulumi.Context, args *GetSnapshotArgs, opts ...pulumi.InvokeOption) (*GetSnapshotResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetSnapshotResult
	err := ctx.Invoke("ionoscloud:index/getSnapshot:getSnapshot", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSnapshot.
type GetSnapshotArgs struct {
	// UUID of an existing snapshot that you want to search for.
	Id *string `pulumi:"id"`
	// Existing snapshot's location.
	Location *string `pulumi:"location"`
	// Name of an existing snapshot that you want to search for.
	Name *string `pulumi:"name"`
	// The size of the snapshot to look for.
	//
	// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	// Additionally, you can add `location` and `size` along with the `name` argument for a more refined search.
	// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
	// When this happens, please refine your search string so that it is specific enough to return only one result.
	Size *int `pulumi:"size"`
}

// A collection of values returned by getSnapshot.
type GetSnapshotResult struct {
	// Is capable of CPU hot plug (no reboot required)
	CpuHotPlug bool `pulumi:"cpuHotPlug"`
	// Is capable of CPU hot unplug (no reboot required)
	CpuHotUnplug bool `pulumi:"cpuHotUnplug"`
	// Human readable description
	Description string `pulumi:"description"`
	// Is capable of SCSI drive hot plug (no reboot required)
	DiscScsiHotPlug bool `pulumi:"discScsiHotPlug"`
	// Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
	DiscScsiHotUnplug bool `pulumi:"discScsiHotUnplug"`
	// Is capable of Virt-IO drive hot plug (no reboot required)
	DiscVirtioHotPlug bool `pulumi:"discVirtioHotPlug"`
	// Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
	DiscVirtioHotUnplug bool `pulumi:"discVirtioHotUnplug"`
	// UUID of the snapshot
	Id *string `pulumi:"id"`
	// OS type of this Snapshot
	LicenceType string `pulumi:"licenceType"`
	// Location of that image/snapshot
	Location string `pulumi:"location"`
	// The name of the snapshot.
	Name string `pulumi:"name"`
	// Is capable of nic hot plug (no reboot required)
	NicHotPlug bool `pulumi:"nicHotPlug"`
	// Is capable of nic hot unplug (no reboot required)
	NicHotUnplug bool `pulumi:"nicHotUnplug"`
	// Is capable of memory hot plug (no reboot required)
	RamHotPlug bool `pulumi:"ramHotPlug"`
	// Is capable of memory hot unplug (no reboot required)
	RamHotUnplug bool `pulumi:"ramHotUnplug"`
	// Boolean value representing if the snapshot requires extra protection e.g. two factor protection
	SecAuthProtection bool `pulumi:"secAuthProtection"`
	// The size of the image in GB
	Size int `pulumi:"size"`
}

func GetSnapshotOutput(ctx *pulumi.Context, args GetSnapshotOutputArgs, opts ...pulumi.InvokeOption) GetSnapshotResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetSnapshotResult, error) {
			args := v.(GetSnapshotArgs)
			r, err := GetSnapshot(ctx, &args, opts...)
			var s GetSnapshotResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetSnapshotResultOutput)
}

// A collection of arguments for invoking getSnapshot.
type GetSnapshotOutputArgs struct {
	// UUID of an existing snapshot that you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Existing snapshot's location.
	Location pulumi.StringPtrInput `pulumi:"location"`
	// Name of an existing snapshot that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The size of the snapshot to look for.
	//
	// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	// Additionally, you can add `location` and `size` along with the `name` argument for a more refined search.
	// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
	// When this happens, please refine your search string so that it is specific enough to return only one result.
	Size pulumi.IntPtrInput `pulumi:"size"`
}

func (GetSnapshotOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSnapshotArgs)(nil)).Elem()
}

// A collection of values returned by getSnapshot.
type GetSnapshotResultOutput struct{ *pulumi.OutputState }

func (GetSnapshotResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSnapshotResult)(nil)).Elem()
}

func (o GetSnapshotResultOutput) ToGetSnapshotResultOutput() GetSnapshotResultOutput {
	return o
}

func (o GetSnapshotResultOutput) ToGetSnapshotResultOutputWithContext(ctx context.Context) GetSnapshotResultOutput {
	return o
}

// Is capable of CPU hot plug (no reboot required)
func (o GetSnapshotResultOutput) CpuHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.CpuHotPlug }).(pulumi.BoolOutput)
}

// Is capable of CPU hot unplug (no reboot required)
func (o GetSnapshotResultOutput) CpuHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.CpuHotUnplug }).(pulumi.BoolOutput)
}

// Human readable description
func (o GetSnapshotResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetSnapshotResult) string { return v.Description }).(pulumi.StringOutput)
}

// Is capable of SCSI drive hot plug (no reboot required)
func (o GetSnapshotResultOutput) DiscScsiHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.DiscScsiHotPlug }).(pulumi.BoolOutput)
}

// Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
func (o GetSnapshotResultOutput) DiscScsiHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.DiscScsiHotUnplug }).(pulumi.BoolOutput)
}

// Is capable of Virt-IO drive hot plug (no reboot required)
func (o GetSnapshotResultOutput) DiscVirtioHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.DiscVirtioHotPlug }).(pulumi.BoolOutput)
}

// Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
func (o GetSnapshotResultOutput) DiscVirtioHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.DiscVirtioHotUnplug }).(pulumi.BoolOutput)
}

// UUID of the snapshot
func (o GetSnapshotResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSnapshotResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// OS type of this Snapshot
func (o GetSnapshotResultOutput) LicenceType() pulumi.StringOutput {
	return o.ApplyT(func(v GetSnapshotResult) string { return v.LicenceType }).(pulumi.StringOutput)
}

// Location of that image/snapshot
func (o GetSnapshotResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v GetSnapshotResult) string { return v.Location }).(pulumi.StringOutput)
}

// The name of the snapshot.
func (o GetSnapshotResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetSnapshotResult) string { return v.Name }).(pulumi.StringOutput)
}

// Is capable of nic hot plug (no reboot required)
func (o GetSnapshotResultOutput) NicHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.NicHotPlug }).(pulumi.BoolOutput)
}

// Is capable of nic hot unplug (no reboot required)
func (o GetSnapshotResultOutput) NicHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.NicHotUnplug }).(pulumi.BoolOutput)
}

// Is capable of memory hot plug (no reboot required)
func (o GetSnapshotResultOutput) RamHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.RamHotPlug }).(pulumi.BoolOutput)
}

// Is capable of memory hot unplug (no reboot required)
func (o GetSnapshotResultOutput) RamHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.RamHotUnplug }).(pulumi.BoolOutput)
}

// Boolean value representing if the snapshot requires extra protection e.g. two factor protection
func (o GetSnapshotResultOutput) SecAuthProtection() pulumi.BoolOutput {
	return o.ApplyT(func(v GetSnapshotResult) bool { return v.SecAuthProtection }).(pulumi.BoolOutput)
}

// The size of the image in GB
func (o GetSnapshotResultOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v GetSnapshotResult) int { return v.Size }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSnapshotResultOutput{})
}

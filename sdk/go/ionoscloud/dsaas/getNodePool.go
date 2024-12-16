// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dsaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupNodePool(ctx *pulumi.Context, args *LookupNodePoolArgs, opts ...pulumi.InvokeOption) (*LookupNodePoolResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNodePoolResult
	err := ctx.Invoke("ionoscloud:dsaas/getNodePool:getNodePool", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNodePool.
type LookupNodePoolArgs struct {
	ClusterId    string  `pulumi:"clusterId"`
	Id           *string `pulumi:"id"`
	Name         *string `pulumi:"name"`
	PartialMatch *bool   `pulumi:"partialMatch"`
}

// A collection of values returned by getNodePool.
type LookupNodePoolResult struct {
	Annotations        map[string]string              `pulumi:"annotations"`
	AvailabilityZone   string                         `pulumi:"availabilityZone"`
	ClusterId          string                         `pulumi:"clusterId"`
	CoresCount         int                            `pulumi:"coresCount"`
	CpuFamily          string                         `pulumi:"cpuFamily"`
	DatacenterId       string                         `pulumi:"datacenterId"`
	Id                 *string                        `pulumi:"id"`
	Labels             map[string]string              `pulumi:"labels"`
	MaintenanceWindows []GetNodePoolMaintenanceWindow `pulumi:"maintenanceWindows"`
	Name               *string                        `pulumi:"name"`
	NodeCount          int                            `pulumi:"nodeCount"`
	PartialMatch       *bool                          `pulumi:"partialMatch"`
	RamSize            int                            `pulumi:"ramSize"`
	StorageSize        int                            `pulumi:"storageSize"`
	StorageType        string                         `pulumi:"storageType"`
	Version            string                         `pulumi:"version"`
}

func LookupNodePoolOutput(ctx *pulumi.Context, args LookupNodePoolOutputArgs, opts ...pulumi.InvokeOption) LookupNodePoolResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupNodePoolResultOutput, error) {
			args := v.(LookupNodePoolArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:dsaas/getNodePool:getNodePool", args, LookupNodePoolResultOutput{}, options).(LookupNodePoolResultOutput), nil
		}).(LookupNodePoolResultOutput)
}

// A collection of arguments for invoking getNodePool.
type LookupNodePoolOutputArgs struct {
	ClusterId    pulumi.StringInput    `pulumi:"clusterId"`
	Id           pulumi.StringPtrInput `pulumi:"id"`
	Name         pulumi.StringPtrInput `pulumi:"name"`
	PartialMatch pulumi.BoolPtrInput   `pulumi:"partialMatch"`
}

func (LookupNodePoolOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNodePoolArgs)(nil)).Elem()
}

// A collection of values returned by getNodePool.
type LookupNodePoolResultOutput struct{ *pulumi.OutputState }

func (LookupNodePoolResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNodePoolResult)(nil)).Elem()
}

func (o LookupNodePoolResultOutput) ToLookupNodePoolResultOutput() LookupNodePoolResultOutput {
	return o
}

func (o LookupNodePoolResultOutput) ToLookupNodePoolResultOutputWithContext(ctx context.Context) LookupNodePoolResultOutput {
	return o
}

func (o LookupNodePoolResultOutput) Annotations() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupNodePoolResult) map[string]string { return v.Annotations }).(pulumi.StringMapOutput)
}

func (o LookupNodePoolResultOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.AvailabilityZone }).(pulumi.StringOutput)
}

func (o LookupNodePoolResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

func (o LookupNodePoolResultOutput) CoresCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNodePoolResult) int { return v.CoresCount }).(pulumi.IntOutput)
}

func (o LookupNodePoolResultOutput) CpuFamily() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.CpuFamily }).(pulumi.StringOutput)
}

func (o LookupNodePoolResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

func (o LookupNodePoolResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNodePoolResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupNodePoolResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupNodePoolResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

func (o LookupNodePoolResultOutput) MaintenanceWindows() GetNodePoolMaintenanceWindowArrayOutput {
	return o.ApplyT(func(v LookupNodePoolResult) []GetNodePoolMaintenanceWindow { return v.MaintenanceWindows }).(GetNodePoolMaintenanceWindowArrayOutput)
}

func (o LookupNodePoolResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNodePoolResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupNodePoolResultOutput) NodeCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNodePoolResult) int { return v.NodeCount }).(pulumi.IntOutput)
}

func (o LookupNodePoolResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupNodePoolResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

func (o LookupNodePoolResultOutput) RamSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNodePoolResult) int { return v.RamSize }).(pulumi.IntOutput)
}

func (o LookupNodePoolResultOutput) StorageSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNodePoolResult) int { return v.StorageSize }).(pulumi.IntOutput)
}

func (o LookupNodePoolResultOutput) StorageType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.StorageType }).(pulumi.StringOutput)
}

func (o LookupNodePoolResultOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.Version }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNodePoolResultOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Returns information about shares of Network File Storage (NFS) on IonosCloud.
func GetNfsShare(ctx *pulumi.Context, args *GetNfsShareArgs, opts ...pulumi.InvokeOption) (*GetNfsShareResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetNfsShareResult
	err := ctx.Invoke("ionoscloud:index/getNfsShare:getNfsShare", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNfsShare.
type GetNfsShareArgs struct {
	// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
	ClientGroups []GetNfsShareClientGroup `pulumi:"clientGroups"`
	// The ID of the Network File Storage cluster.
	ClusterId string `pulumi:"clusterId"`
	// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Gid *int `pulumi:"gid"`
	// ID of the Network File Storage share.
	Id *string `pulumi:"id"`
	// The location where the Network File Storage share is located.
	Location string `pulumi:"location"`
	// Name of the Network File Storage share.
	Name *string `pulumi:"name"`
	// Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
	PartialMatch *bool `pulumi:"partialMatch"`
	// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
	Quota *int `pulumi:"quota"`
	// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Uid *int `pulumi:"uid"`
}

// A collection of values returned by getNfsShare.
type GetNfsShareResult struct {
	// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
	ClientGroups []GetNfsShareClientGroup `pulumi:"clientGroups"`
	// The ID of the Network File Storage cluster.
	ClusterId string `pulumi:"clusterId"`
	// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Gid int `pulumi:"gid"`
	// The ID of the Network File Storage share.
	Id string `pulumi:"id"`
	// The location where the Network File Storage share is located.
	Location string `pulumi:"location"`
	// The name of the Network File Storage share.
	Name string `pulumi:"name"`
	// Path to the NFS export. The NFS path is the path to the directory being exported.
	NfsPath      string `pulumi:"nfsPath"`
	PartialMatch *bool  `pulumi:"partialMatch"`
	// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
	Quota int `pulumi:"quota"`
	// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Uid int `pulumi:"uid"`
}

func GetNfsShareOutput(ctx *pulumi.Context, args GetNfsShareOutputArgs, opts ...pulumi.InvokeOption) GetNfsShareResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetNfsShareResultOutput, error) {
			args := v.(GetNfsShareArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getNfsShare:getNfsShare", args, GetNfsShareResultOutput{}, options).(GetNfsShareResultOutput), nil
		}).(GetNfsShareResultOutput)
}

// A collection of arguments for invoking getNfsShare.
type GetNfsShareOutputArgs struct {
	// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
	ClientGroups GetNfsShareClientGroupArrayInput `pulumi:"clientGroups"`
	// The ID of the Network File Storage cluster.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Gid pulumi.IntPtrInput `pulumi:"gid"`
	// ID of the Network File Storage share.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The location where the Network File Storage share is located.
	Location pulumi.StringInput `pulumi:"location"`
	// Name of the Network File Storage share.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
	PartialMatch pulumi.BoolPtrInput `pulumi:"partialMatch"`
	// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
	Quota pulumi.IntPtrInput `pulumi:"quota"`
	// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Uid pulumi.IntPtrInput `pulumi:"uid"`
}

func (GetNfsShareOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetNfsShareArgs)(nil)).Elem()
}

// A collection of values returned by getNfsShare.
type GetNfsShareResultOutput struct{ *pulumi.OutputState }

func (GetNfsShareResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetNfsShareResult)(nil)).Elem()
}

func (o GetNfsShareResultOutput) ToGetNfsShareResultOutput() GetNfsShareResultOutput {
	return o
}

func (o GetNfsShareResultOutput) ToGetNfsShareResultOutputWithContext(ctx context.Context) GetNfsShareResultOutput {
	return o
}

// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
func (o GetNfsShareResultOutput) ClientGroups() GetNfsShareClientGroupArrayOutput {
	return o.ApplyT(func(v GetNfsShareResult) []GetNfsShareClientGroup { return v.ClientGroups }).(GetNfsShareClientGroupArrayOutput)
}

// The ID of the Network File Storage cluster.
func (o GetNfsShareResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetNfsShareResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
func (o GetNfsShareResultOutput) Gid() pulumi.IntOutput {
	return o.ApplyT(func(v GetNfsShareResult) int { return v.Gid }).(pulumi.IntOutput)
}

// The ID of the Network File Storage share.
func (o GetNfsShareResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetNfsShareResult) string { return v.Id }).(pulumi.StringOutput)
}

// The location where the Network File Storage share is located.
func (o GetNfsShareResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v GetNfsShareResult) string { return v.Location }).(pulumi.StringOutput)
}

// The name of the Network File Storage share.
func (o GetNfsShareResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetNfsShareResult) string { return v.Name }).(pulumi.StringOutput)
}

// Path to the NFS export. The NFS path is the path to the directory being exported.
func (o GetNfsShareResultOutput) NfsPath() pulumi.StringOutput {
	return o.ApplyT(func(v GetNfsShareResult) string { return v.NfsPath }).(pulumi.StringOutput)
}

func (o GetNfsShareResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v GetNfsShareResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
func (o GetNfsShareResultOutput) Quota() pulumi.IntOutput {
	return o.ApplyT(func(v GetNfsShareResult) int { return v.Quota }).(pulumi.IntOutput)
}

// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
func (o GetNfsShareResultOutput) Uid() pulumi.IntOutput {
	return o.ApplyT(func(v GetNfsShareResult) int { return v.Uid }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(GetNfsShareResultOutput{})
}

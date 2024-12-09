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
func LookupNfsShare(ctx *pulumi.Context, args *LookupNfsShareArgs, opts ...pulumi.InvokeOption) (*LookupNfsShareResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNfsShareResult
	err := ctx.Invoke("ionoscloud:index/getNfsShare:getNfsShare", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNfsShare.
type LookupNfsShareArgs struct {
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
type LookupNfsShareResult struct {
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

func LookupNfsShareOutput(ctx *pulumi.Context, args LookupNfsShareOutputArgs, opts ...pulumi.InvokeOption) LookupNfsShareResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNfsShareResultOutput, error) {
			args := v.(LookupNfsShareArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupNfsShareResult
			secret, err := ctx.InvokePackageRaw("ionoscloud:index/getNfsShare:getNfsShare", args, &rv, "", opts...)
			if err != nil {
				return LookupNfsShareResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupNfsShareResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupNfsShareResultOutput), nil
			}
			return output, nil
		}).(LookupNfsShareResultOutput)
}

// A collection of arguments for invoking getNfsShare.
type LookupNfsShareOutputArgs struct {
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

func (LookupNfsShareOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNfsShareArgs)(nil)).Elem()
}

// A collection of values returned by getNfsShare.
type LookupNfsShareResultOutput struct{ *pulumi.OutputState }

func (LookupNfsShareResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNfsShareResult)(nil)).Elem()
}

func (o LookupNfsShareResultOutput) ToLookupNfsShareResultOutput() LookupNfsShareResultOutput {
	return o
}

func (o LookupNfsShareResultOutput) ToLookupNfsShareResultOutputWithContext(ctx context.Context) LookupNfsShareResultOutput {
	return o
}

// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
func (o LookupNfsShareResultOutput) ClientGroups() GetNfsShareClientGroupArrayOutput {
	return o.ApplyT(func(v LookupNfsShareResult) []GetNfsShareClientGroup { return v.ClientGroups }).(GetNfsShareClientGroupArrayOutput)
}

// The ID of the Network File Storage cluster.
func (o LookupNfsShareResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNfsShareResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
func (o LookupNfsShareResultOutput) Gid() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNfsShareResult) int { return v.Gid }).(pulumi.IntOutput)
}

// The ID of the Network File Storage share.
func (o LookupNfsShareResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNfsShareResult) string { return v.Id }).(pulumi.StringOutput)
}

// The location where the Network File Storage share is located.
func (o LookupNfsShareResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNfsShareResult) string { return v.Location }).(pulumi.StringOutput)
}

// The name of the Network File Storage share.
func (o LookupNfsShareResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNfsShareResult) string { return v.Name }).(pulumi.StringOutput)
}

// Path to the NFS export. The NFS path is the path to the directory being exported.
func (o LookupNfsShareResultOutput) NfsPath() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNfsShareResult) string { return v.NfsPath }).(pulumi.StringOutput)
}

func (o LookupNfsShareResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupNfsShareResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
func (o LookupNfsShareResultOutput) Quota() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNfsShareResult) int { return v.Quota }).(pulumi.IntOutput)
}

// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
func (o LookupNfsShareResultOutput) Uid() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNfsShareResult) int { return v.Uid }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNfsShareResultOutput{})
}

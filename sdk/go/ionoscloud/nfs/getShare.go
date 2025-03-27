// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package nfs

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Returns information about shares of Network File Storage (NFS) on IonosCloud.
//
// ## By ID
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/nfs"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := nfs.LookupShare(ctx, &nfs.LookupShareArgs{
//				Location:  pulumi.StringRef("location"),
//				ClusterId: "cluster-id",
//				Id:        pulumi.StringRef("share-id"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## By Name
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/nfs"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := nfs.LookupShare(ctx, &nfs.LookupShareArgs{
//				Location:     pulumi.StringRef("location"),
//				ClusterId:    "cluster-id",
//				Name:         pulumi.StringRef("partial-name"),
//				PartialMatch: pulumi.BoolRef(true),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupShare(ctx *pulumi.Context, args *LookupShareArgs, opts ...pulumi.InvokeOption) (*LookupShareResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupShareResult
	err := ctx.Invoke("ionoscloud:nfs/getShare:getShare", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getShare.
type LookupShareArgs struct {
	// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
	ClientGroups []GetShareClientGroup `pulumi:"clientGroups"`
	// The ID of the Network File Storage cluster.
	ClusterId string `pulumi:"clusterId"`
	// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Gid *int `pulumi:"gid"`
	// ID of the Network File Storage share.
	Id *string `pulumi:"id"`
	// The location where the Network File Storage share is located.
	Location *string `pulumi:"location"`
	// Name of the Network File Storage share.
	Name *string `pulumi:"name"`
	// Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
	PartialMatch *bool `pulumi:"partialMatch"`
	// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
	Quota *int `pulumi:"quota"`
	// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Uid *int `pulumi:"uid"`
}

// A collection of values returned by getShare.
type LookupShareResult struct {
	// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
	ClientGroups []GetShareClientGroup `pulumi:"clientGroups"`
	// The ID of the Network File Storage cluster.
	ClusterId string `pulumi:"clusterId"`
	// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Gid int `pulumi:"gid"`
	// The ID of the Network File Storage share.
	Id string `pulumi:"id"`
	// The location where the Network File Storage share is located.
	Location *string `pulumi:"location"`
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

func LookupShareOutput(ctx *pulumi.Context, args LookupShareOutputArgs, opts ...pulumi.InvokeOption) LookupShareResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupShareResultOutput, error) {
			args := v.(LookupShareArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:nfs/getShare:getShare", args, LookupShareResultOutput{}, options).(LookupShareResultOutput), nil
		}).(LookupShareResultOutput)
}

// A collection of arguments for invoking getShare.
type LookupShareOutputArgs struct {
	// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
	ClientGroups GetShareClientGroupArrayInput `pulumi:"clientGroups"`
	// The ID of the Network File Storage cluster.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Gid pulumi.IntPtrInput `pulumi:"gid"`
	// ID of the Network File Storage share.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The location where the Network File Storage share is located.
	Location pulumi.StringPtrInput `pulumi:"location"`
	// Name of the Network File Storage share.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
	PartialMatch pulumi.BoolPtrInput `pulumi:"partialMatch"`
	// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
	Quota pulumi.IntPtrInput `pulumi:"quota"`
	// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
	Uid pulumi.IntPtrInput `pulumi:"uid"`
}

func (LookupShareOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupShareArgs)(nil)).Elem()
}

// A collection of values returned by getShare.
type LookupShareResultOutput struct{ *pulumi.OutputState }

func (LookupShareResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupShareResult)(nil)).Elem()
}

func (o LookupShareResultOutput) ToLookupShareResultOutput() LookupShareResultOutput {
	return o
}

func (o LookupShareResultOutput) ToLookupShareResultOutputWithContext(ctx context.Context) LookupShareResultOutput {
	return o
}

// The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
func (o LookupShareResultOutput) ClientGroups() GetShareClientGroupArrayOutput {
	return o.ApplyT(func(v LookupShareResult) []GetShareClientGroup { return v.ClientGroups }).(GetShareClientGroupArrayOutput)
}

// The ID of the Network File Storage cluster.
func (o LookupShareResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupShareResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
func (o LookupShareResultOutput) Gid() pulumi.IntOutput {
	return o.ApplyT(func(v LookupShareResult) int { return v.Gid }).(pulumi.IntOutput)
}

// The ID of the Network File Storage share.
func (o LookupShareResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupShareResult) string { return v.Id }).(pulumi.StringOutput)
}

// The location where the Network File Storage share is located.
func (o LookupShareResultOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupShareResult) *string { return v.Location }).(pulumi.StringPtrOutput)
}

// The name of the Network File Storage share.
func (o LookupShareResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupShareResult) string { return v.Name }).(pulumi.StringOutput)
}

// Path to the NFS export. The NFS path is the path to the directory being exported.
func (o LookupShareResultOutput) NfsPath() pulumi.StringOutput {
	return o.ApplyT(func(v LookupShareResult) string { return v.NfsPath }).(pulumi.StringOutput)
}

func (o LookupShareResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupShareResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
func (o LookupShareResultOutput) Quota() pulumi.IntOutput {
	return o.ApplyT(func(v LookupShareResult) int { return v.Quota }).(pulumi.IntOutput)
}

// The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
func (o LookupShareResultOutput) Uid() pulumi.IntOutput {
	return o.ApplyT(func(v LookupShareResult) int { return v.Uid }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupShareResultOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package nfs

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Returns information about clusters of Network File Storage (NFS) on IonosCloud.
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
//			_, err := nfs.LookupCluster(ctx, &nfs.LookupClusterArgs{
//				Location: "location",
//				Id:       pulumi.StringRef("cluster-id"),
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
//			_, err := nfs.LookupCluster(ctx, &nfs.LookupClusterArgs{
//				Location:     "location",
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
func LookupCluster(ctx *pulumi.Context, args *LookupClusterArgs, opts ...pulumi.InvokeOption) (*LookupClusterResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupClusterResult
	err := ctx.Invoke("ionoscloud:nfs/getCluster:getCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCluster.
type LookupClusterArgs struct {
	// ID of the Network File Storage cluster.
	Id *string `pulumi:"id"`
	// The location where the Network File Storage cluster is located.
	Location string `pulumi:"location"`
	// Name of the Network File Storage cluster.
	Name *string `pulumi:"name"`
	// Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
	PartialMatch *bool `pulumi:"partialMatch"`
}

// A collection of values returned by getCluster.
type LookupClusterResult struct {
	// A list of connections for the Network File Storage cluster. You can specify only one connection. Each connection supports the following:
	Connections []GetClusterConnection `pulumi:"connections"`
	// The ID of the Network File Storage cluster.
	Id string `pulumi:"id"`
	// The location where the Network File Storage cluster is located.
	Location string `pulumi:"location"`
	// The name of the Network File Storage cluster.
	Name string `pulumi:"name"`
	// The NFS configuration for the Network File Storage cluster. Each NFS configuration supports the following:
	Nfs          []GetClusterNf `pulumi:"nfs"`
	PartialMatch *bool          `pulumi:"partialMatch"`
	// The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
	Size int `pulumi:"size"`
}

func LookupClusterOutput(ctx *pulumi.Context, args LookupClusterOutputArgs, opts ...pulumi.InvokeOption) LookupClusterResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupClusterResultOutput, error) {
			args := v.(LookupClusterArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:nfs/getCluster:getCluster", args, LookupClusterResultOutput{}, options).(LookupClusterResultOutput), nil
		}).(LookupClusterResultOutput)
}

// A collection of arguments for invoking getCluster.
type LookupClusterOutputArgs struct {
	// ID of the Network File Storage cluster.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The location where the Network File Storage cluster is located.
	Location pulumi.StringInput `pulumi:"location"`
	// Name of the Network File Storage cluster.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
	PartialMatch pulumi.BoolPtrInput `pulumi:"partialMatch"`
}

func (LookupClusterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupClusterArgs)(nil)).Elem()
}

// A collection of values returned by getCluster.
type LookupClusterResultOutput struct{ *pulumi.OutputState }

func (LookupClusterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupClusterResult)(nil)).Elem()
}

func (o LookupClusterResultOutput) ToLookupClusterResultOutput() LookupClusterResultOutput {
	return o
}

func (o LookupClusterResultOutput) ToLookupClusterResultOutputWithContext(ctx context.Context) LookupClusterResultOutput {
	return o
}

// A list of connections for the Network File Storage cluster. You can specify only one connection. Each connection supports the following:
func (o LookupClusterResultOutput) Connections() GetClusterConnectionArrayOutput {
	return o.ApplyT(func(v LookupClusterResult) []GetClusterConnection { return v.Connections }).(GetClusterConnectionArrayOutput)
}

// The ID of the Network File Storage cluster.
func (o LookupClusterResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupClusterResult) string { return v.Id }).(pulumi.StringOutput)
}

// The location where the Network File Storage cluster is located.
func (o LookupClusterResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupClusterResult) string { return v.Location }).(pulumi.StringOutput)
}

// The name of the Network File Storage cluster.
func (o LookupClusterResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupClusterResult) string { return v.Name }).(pulumi.StringOutput)
}

// The NFS configuration for the Network File Storage cluster. Each NFS configuration supports the following:
func (o LookupClusterResultOutput) Nfs() GetClusterNfArrayOutput {
	return o.ApplyT(func(v LookupClusterResult) []GetClusterNf { return v.Nfs }).(GetClusterNfArrayOutput)
}

func (o LookupClusterResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupClusterResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
func (o LookupClusterResultOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v LookupClusterResult) int { return v.Size }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupClusterResultOutput{})
}

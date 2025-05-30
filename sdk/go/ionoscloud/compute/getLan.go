// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **LAN data source** can be used to search for and return existing lans.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By ID
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := compute.LookupLan(ctx, &compute.LookupLanArgs{
//				DatacenterId: "datacenter_id",
//				Id:           pulumi.StringRef("lan_id"),
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
// ### By Name
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := compute.LookupLan(ctx, &compute.LookupLanArgs{
//				DatacenterId: "datacenter_id",
//				Name:         pulumi.StringRef("Lan Example"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupLan(ctx *pulumi.Context, args *LookupLanArgs, opts ...pulumi.InvokeOption) (*LookupLanResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLanResult
	err := ctx.Invoke("ionoscloud:compute/getLan:getLan", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLan.
type LookupLanArgs struct {
	// Datacenter's UUID.
	DatacenterId string `pulumi:"datacenterId"`
	// ID of the lan you want to search for.
	//
	// `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// Name of an existing lan that you want to search for.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getLan.
type LookupLanResult struct {
	// The ID of lan's Virtual Data Center.
	DatacenterId string `pulumi:"datacenterId"`
	// The id of the LAN.
	Id string `pulumi:"id"`
	// list of
	IpFailovers []GetLanIpFailover `pulumi:"ipFailovers"`
	// For public LANs this property is null, for private LANs it contains the private IPv4 CIDR range.
	Ipv4CidrBlock string `pulumi:"ipv4CidrBlock"`
	// Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled.
	Ipv6CidrBlock string `pulumi:"ipv6CidrBlock"`
	// The name of the LAN.
	Name string `pulumi:"name"`
	// The unique id of a `compute.Crossconnect` resource, in order.
	Pcc string `pulumi:"pcc"`
	// Indicates if the LAN faces the public Internet (true) or not (false).
	Public bool `pulumi:"public"`
}

func LookupLanOutput(ctx *pulumi.Context, args LookupLanOutputArgs, opts ...pulumi.InvokeOption) LookupLanResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupLanResultOutput, error) {
			args := v.(LookupLanArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:compute/getLan:getLan", args, LookupLanResultOutput{}, options).(LookupLanResultOutput), nil
		}).(LookupLanResultOutput)
}

// A collection of arguments for invoking getLan.
type LookupLanOutputArgs struct {
	// Datacenter's UUID.
	DatacenterId pulumi.StringInput `pulumi:"datacenterId"`
	// ID of the lan you want to search for.
	//
	// `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing lan that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupLanOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLanArgs)(nil)).Elem()
}

// A collection of values returned by getLan.
type LookupLanResultOutput struct{ *pulumi.OutputState }

func (LookupLanResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLanResult)(nil)).Elem()
}

func (o LookupLanResultOutput) ToLookupLanResultOutput() LookupLanResultOutput {
	return o
}

func (o LookupLanResultOutput) ToLookupLanResultOutputWithContext(ctx context.Context) LookupLanResultOutput {
	return o
}

// The ID of lan's Virtual Data Center.
func (o LookupLanResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLanResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// The id of the LAN.
func (o LookupLanResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLanResult) string { return v.Id }).(pulumi.StringOutput)
}

// list of
func (o LookupLanResultOutput) IpFailovers() GetLanIpFailoverArrayOutput {
	return o.ApplyT(func(v LookupLanResult) []GetLanIpFailover { return v.IpFailovers }).(GetLanIpFailoverArrayOutput)
}

// For public LANs this property is null, for private LANs it contains the private IPv4 CIDR range.
func (o LookupLanResultOutput) Ipv4CidrBlock() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLanResult) string { return v.Ipv4CidrBlock }).(pulumi.StringOutput)
}

// Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled.
func (o LookupLanResultOutput) Ipv6CidrBlock() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLanResult) string { return v.Ipv6CidrBlock }).(pulumi.StringOutput)
}

// The name of the LAN.
func (o LookupLanResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLanResult) string { return v.Name }).(pulumi.StringOutput)
}

// The unique id of a `compute.Crossconnect` resource, in order.
func (o LookupLanResultOutput) Pcc() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLanResult) string { return v.Pcc }).(pulumi.StringOutput)
}

// Indicates if the LAN faces the public Internet (true) or not (false).
func (o LookupLanResultOutput) Public() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupLanResult) bool { return v.Public }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLanResultOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **IP Block data source** can be used to search for and return an existing Ip Block.
// You can provide a string for the id, the name or the location parameters which will be compared with the provisioned Ip Blocks.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By Name
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
//			_, err := ionoscloud.LookupIpblock(ctx, &ionoscloud.LookupIpblockArgs{
//				Name: pulumi.StringRef("IP Block Name"),
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
//
// ### By Location
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
//			_, err := ionoscloud.LookupIpblock(ctx, &ionoscloud.LookupIpblockArgs{
//				Location: pulumi.StringRef("us/las"),
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
//
// ### By Name & Location
func LookupIpblock(ctx *pulumi.Context, args *LookupIpblockArgs, opts ...pulumi.InvokeOption) (*LookupIpblockResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupIpblockResult
	err := ctx.Invoke("ionoscloud:index/getIpblock:getIpblock", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getIpblock.
type LookupIpblockArgs struct {
	// ID of an existing Ip Block that you want to search for.
	Id *string `pulumi:"id"`
	// Read-Only attribute. Lists consumption detail of an individual ip
	IpConsumers []GetIpblockIpConsumer `pulumi:"ipConsumers"`
	// The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
	Location *string `pulumi:"location"`
	// Name of an existing Ip Block that you want to search for.
	Name *string `pulumi:"name"`
	// The number of IP addresses to reserve for this block.
	Size *int `pulumi:"size"`
}

// A collection of values returned by getIpblock.
type LookupIpblockResult struct {
	// The id of Ip Block
	Id *string `pulumi:"id"`
	// Read-Only attribute. Lists consumption detail of an individual ip
	IpConsumers []GetIpblockIpConsumer `pulumi:"ipConsumers"`
	// The list of IP addresses associated with this block.
	Ips []string `pulumi:"ips"`
	// The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
	Location *string `pulumi:"location"`
	// The name of Ip Block
	Name *string `pulumi:"name"`
	// The number of IP addresses to reserve for this block.
	Size *int `pulumi:"size"`
}

func LookupIpblockOutput(ctx *pulumi.Context, args LookupIpblockOutputArgs, opts ...pulumi.InvokeOption) LookupIpblockResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupIpblockResult, error) {
			args := v.(LookupIpblockArgs)
			r, err := LookupIpblock(ctx, &args, opts...)
			var s LookupIpblockResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupIpblockResultOutput)
}

// A collection of arguments for invoking getIpblock.
type LookupIpblockOutputArgs struct {
	// ID of an existing Ip Block that you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Read-Only attribute. Lists consumption detail of an individual ip
	IpConsumers GetIpblockIpConsumerArrayInput `pulumi:"ipConsumers"`
	// The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
	Location pulumi.StringPtrInput `pulumi:"location"`
	// Name of an existing Ip Block that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The number of IP addresses to reserve for this block.
	Size pulumi.IntPtrInput `pulumi:"size"`
}

func (LookupIpblockOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpblockArgs)(nil)).Elem()
}

// A collection of values returned by getIpblock.
type LookupIpblockResultOutput struct{ *pulumi.OutputState }

func (LookupIpblockResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpblockResult)(nil)).Elem()
}

func (o LookupIpblockResultOutput) ToLookupIpblockResultOutput() LookupIpblockResultOutput {
	return o
}

func (o LookupIpblockResultOutput) ToLookupIpblockResultOutputWithContext(ctx context.Context) LookupIpblockResultOutput {
	return o
}

// The id of Ip Block
func (o LookupIpblockResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpblockResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Read-Only attribute. Lists consumption detail of an individual ip
func (o LookupIpblockResultOutput) IpConsumers() GetIpblockIpConsumerArrayOutput {
	return o.ApplyT(func(v LookupIpblockResult) []GetIpblockIpConsumer { return v.IpConsumers }).(GetIpblockIpConsumerArrayOutput)
}

// The list of IP addresses associated with this block.
func (o LookupIpblockResultOutput) Ips() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupIpblockResult) []string { return v.Ips }).(pulumi.StringArrayOutput)
}

// The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
func (o LookupIpblockResultOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpblockResult) *string { return v.Location }).(pulumi.StringPtrOutput)
}

// The name of Ip Block
func (o LookupIpblockResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpblockResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The number of IP addresses to reserve for this block.
func (o LookupIpblockResultOutput) Size() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupIpblockResult) *int { return v.Size }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupIpblockResultOutput{})
}

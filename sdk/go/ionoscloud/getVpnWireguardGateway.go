// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The `VpnWireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.
//
// ## Example Usage
//
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
//			_, err := ionoscloud.LookupVpnWireguardGateway(ctx, &ionoscloud.LookupVpnWireguardGatewayArgs{
//				Location: "de/fra",
//				Name:     pulumi.StringRef("example-gateway"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("vpnWireguardGatewayPublicKey", data.Vpn_wireguard_gateway.Example.Public_key)
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
func LookupVpnWireguardGateway(ctx *pulumi.Context, args *LookupVpnWireguardGatewayArgs, opts ...pulumi.InvokeOption) (*LookupVpnWireguardGatewayResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVpnWireguardGatewayResult
	err := ctx.Invoke("ionoscloud:index/getVpnWireguardGateway:getVpnWireguardGateway", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVpnWireguardGateway.
type LookupVpnWireguardGatewayArgs struct {
	// The description of the WireGuard Gateway.
	Description *string `pulumi:"description"`
	// [String] The ID of the WireGuard Gateway.
	Id *string `pulumi:"id"`
	// [String] The location of the WireGuard Gateway.
	Location string `pulumi:"location"`
	// [String] The name of the WireGuard Gateway.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getVpnWireguardGateway.
type LookupVpnWireguardGatewayResult struct {
	// A list of connection configurations for the WireGuard Gateway. Each `connections` block contains:
	Connections []GetVpnWireguardGatewayConnection `pulumi:"connections"`
	// The description of the WireGuard Gateway.
	Description *string `pulumi:"description"`
	// The IP address of the WireGuard Gateway.
	GatewayIp string `pulumi:"gatewayIp"`
	Id        string `pulumi:"id"`
	// The IPv4 CIDR for the WireGuard Gateway interface.
	InterfaceIpv4Cidr string `pulumi:"interfaceIpv4Cidr"`
	// The IPv6 CIDR for the WireGuard Gateway interface.
	InterfaceIpv6Cidr string `pulumi:"interfaceIpv6Cidr"`
	ListenPort        int    `pulumi:"listenPort"`
	Location          string `pulumi:"location"`
	Name              string `pulumi:"name"`
	// The public key for the WireGuard Gateway.
	PublicKey string `pulumi:"publicKey"`
	// The current status of the WireGuard Gateway.
	Status string `pulumi:"status"`
}

func LookupVpnWireguardGatewayOutput(ctx *pulumi.Context, args LookupVpnWireguardGatewayOutputArgs, opts ...pulumi.InvokeOption) LookupVpnWireguardGatewayResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVpnWireguardGatewayResult, error) {
			args := v.(LookupVpnWireguardGatewayArgs)
			r, err := LookupVpnWireguardGateway(ctx, &args, opts...)
			var s LookupVpnWireguardGatewayResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVpnWireguardGatewayResultOutput)
}

// A collection of arguments for invoking getVpnWireguardGateway.
type LookupVpnWireguardGatewayOutputArgs struct {
	// The description of the WireGuard Gateway.
	Description pulumi.StringPtrInput `pulumi:"description"`
	// [String] The ID of the WireGuard Gateway.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// [String] The location of the WireGuard Gateway.
	Location pulumi.StringInput `pulumi:"location"`
	// [String] The name of the WireGuard Gateway.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupVpnWireguardGatewayOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpnWireguardGatewayArgs)(nil)).Elem()
}

// A collection of values returned by getVpnWireguardGateway.
type LookupVpnWireguardGatewayResultOutput struct{ *pulumi.OutputState }

func (LookupVpnWireguardGatewayResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpnWireguardGatewayResult)(nil)).Elem()
}

func (o LookupVpnWireguardGatewayResultOutput) ToLookupVpnWireguardGatewayResultOutput() LookupVpnWireguardGatewayResultOutput {
	return o
}

func (o LookupVpnWireguardGatewayResultOutput) ToLookupVpnWireguardGatewayResultOutputWithContext(ctx context.Context) LookupVpnWireguardGatewayResultOutput {
	return o
}

// A list of connection configurations for the WireGuard Gateway. Each `connections` block contains:
func (o LookupVpnWireguardGatewayResultOutput) Connections() GetVpnWireguardGatewayConnectionArrayOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) []GetVpnWireguardGatewayConnection { return v.Connections }).(GetVpnWireguardGatewayConnectionArrayOutput)
}

// The description of the WireGuard Gateway.
func (o LookupVpnWireguardGatewayResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The IP address of the WireGuard Gateway.
func (o LookupVpnWireguardGatewayResultOutput) GatewayIp() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) string { return v.GatewayIp }).(pulumi.StringOutput)
}

func (o LookupVpnWireguardGatewayResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) string { return v.Id }).(pulumi.StringOutput)
}

// The IPv4 CIDR for the WireGuard Gateway interface.
func (o LookupVpnWireguardGatewayResultOutput) InterfaceIpv4Cidr() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) string { return v.InterfaceIpv4Cidr }).(pulumi.StringOutput)
}

// The IPv6 CIDR for the WireGuard Gateway interface.
func (o LookupVpnWireguardGatewayResultOutput) InterfaceIpv6Cidr() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) string { return v.InterfaceIpv6Cidr }).(pulumi.StringOutput)
}

func (o LookupVpnWireguardGatewayResultOutput) ListenPort() pulumi.IntOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) int { return v.ListenPort }).(pulumi.IntOutput)
}

func (o LookupVpnWireguardGatewayResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) string { return v.Location }).(pulumi.StringOutput)
}

func (o LookupVpnWireguardGatewayResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) string { return v.Name }).(pulumi.StringOutput)
}

// The public key for the WireGuard Gateway.
func (o LookupVpnWireguardGatewayResultOutput) PublicKey() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) string { return v.PublicKey }).(pulumi.StringOutput)
}

// The current status of the WireGuard Gateway.
func (o LookupVpnWireguardGatewayResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnWireguardGatewayResult) string { return v.Status }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVpnWireguardGatewayResultOutput{})
}

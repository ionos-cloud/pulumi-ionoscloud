// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **VPN IPSec Gateway Tunnel data source** can be used to search for and return an existing IPSec Gateway Tunnel.
// You can provide a string for the name parameter which will be compared with provisioned IPSec Gateway Tunnels.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
func LookupVpnIpsecTunnel(ctx *pulumi.Context, args *LookupVpnIpsecTunnelArgs, opts ...pulumi.InvokeOption) (*LookupVpnIpsecTunnelResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVpnIpsecTunnelResult
	err := ctx.Invoke("ionoscloud:index/getVpnIpsecTunnel:getVpnIpsecTunnel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVpnIpsecTunnel.
type LookupVpnIpsecTunnelArgs struct {
	// The ID of the IPSec Gateway that the tunnel belongs to.
	GatewayId string `pulumi:"gatewayId"`
	// ID of an existing IPSec Gateway Tunnel that you want to search for.
	Id *string `pulumi:"id"`
	// The location of the IPSec Gateway Tunnel.
	Location string `pulumi:"location"`
	// Name of an existing IPSec Gateway Tunnel that you want to search for.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getVpnIpsecTunnel.
type LookupVpnIpsecTunnelResult struct {
	Auths             []GetVpnIpsecTunnelAuth `pulumi:"auths"`
	CloudNetworkCidrs []string                `pulumi:"cloudNetworkCidrs"`
	Description       string                  `pulumi:"description"`
	Esps              []GetVpnIpsecTunnelEsp  `pulumi:"esps"`
	GatewayId         string                  `pulumi:"gatewayId"`
	Id                string                  `pulumi:"id"`
	Ikes              []GetVpnIpsecTunnelIke  `pulumi:"ikes"`
	Location          string                  `pulumi:"location"`
	Name              string                  `pulumi:"name"`
	PeerNetworkCidrs  []string                `pulumi:"peerNetworkCidrs"`
	RemoteHost        string                  `pulumi:"remoteHost"`
}

func LookupVpnIpsecTunnelOutput(ctx *pulumi.Context, args LookupVpnIpsecTunnelOutputArgs, opts ...pulumi.InvokeOption) LookupVpnIpsecTunnelResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVpnIpsecTunnelResultOutput, error) {
			args := v.(LookupVpnIpsecTunnelArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupVpnIpsecTunnelResult
			secret, err := ctx.InvokePackageRaw("ionoscloud:index/getVpnIpsecTunnel:getVpnIpsecTunnel", args, &rv, "", opts...)
			if err != nil {
				return LookupVpnIpsecTunnelResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupVpnIpsecTunnelResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupVpnIpsecTunnelResultOutput), nil
			}
			return output, nil
		}).(LookupVpnIpsecTunnelResultOutput)
}

// A collection of arguments for invoking getVpnIpsecTunnel.
type LookupVpnIpsecTunnelOutputArgs struct {
	// The ID of the IPSec Gateway that the tunnel belongs to.
	GatewayId pulumi.StringInput `pulumi:"gatewayId"`
	// ID of an existing IPSec Gateway Tunnel that you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The location of the IPSec Gateway Tunnel.
	Location pulumi.StringInput `pulumi:"location"`
	// Name of an existing IPSec Gateway Tunnel that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupVpnIpsecTunnelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpnIpsecTunnelArgs)(nil)).Elem()
}

// A collection of values returned by getVpnIpsecTunnel.
type LookupVpnIpsecTunnelResultOutput struct{ *pulumi.OutputState }

func (LookupVpnIpsecTunnelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpnIpsecTunnelResult)(nil)).Elem()
}

func (o LookupVpnIpsecTunnelResultOutput) ToLookupVpnIpsecTunnelResultOutput() LookupVpnIpsecTunnelResultOutput {
	return o
}

func (o LookupVpnIpsecTunnelResultOutput) ToLookupVpnIpsecTunnelResultOutputWithContext(ctx context.Context) LookupVpnIpsecTunnelResultOutput {
	return o
}

func (o LookupVpnIpsecTunnelResultOutput) Auths() GetVpnIpsecTunnelAuthArrayOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) []GetVpnIpsecTunnelAuth { return v.Auths }).(GetVpnIpsecTunnelAuthArrayOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) CloudNetworkCidrs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) []string { return v.CloudNetworkCidrs }).(pulumi.StringArrayOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) Esps() GetVpnIpsecTunnelEspArrayOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) []GetVpnIpsecTunnelEsp { return v.Esps }).(GetVpnIpsecTunnelEspArrayOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) GatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) string { return v.GatewayId }).(pulumi.StringOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) Ikes() GetVpnIpsecTunnelIkeArrayOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) []GetVpnIpsecTunnelIke { return v.Ikes }).(GetVpnIpsecTunnelIkeArrayOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) string { return v.Location }).(pulumi.StringOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) PeerNetworkCidrs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) []string { return v.PeerNetworkCidrs }).(pulumi.StringArrayOutput)
}

func (o LookupVpnIpsecTunnelResultOutput) RemoteHost() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpnIpsecTunnelResult) string { return v.RemoteHost }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVpnIpsecTunnelResultOutput{})
}

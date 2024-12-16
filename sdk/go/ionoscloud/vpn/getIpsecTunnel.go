// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpn

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupIpsecTunnel(ctx *pulumi.Context, args *LookupIpsecTunnelArgs, opts ...pulumi.InvokeOption) (*LookupIpsecTunnelResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupIpsecTunnelResult
	err := ctx.Invoke("ionoscloud:vpn/getIpsecTunnel:getIpsecTunnel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getIpsecTunnel.
type LookupIpsecTunnelArgs struct {
	GatewayId string  `pulumi:"gatewayId"`
	Id        *string `pulumi:"id"`
	Location  string  `pulumi:"location"`
	Name      *string `pulumi:"name"`
}

// A collection of values returned by getIpsecTunnel.
type LookupIpsecTunnelResult struct {
	Auths             []GetIpsecTunnelAuth `pulumi:"auths"`
	CloudNetworkCidrs []string             `pulumi:"cloudNetworkCidrs"`
	Description       string               `pulumi:"description"`
	Esps              []GetIpsecTunnelEsp  `pulumi:"esps"`
	GatewayId         string               `pulumi:"gatewayId"`
	Id                string               `pulumi:"id"`
	Ikes              []GetIpsecTunnelIke  `pulumi:"ikes"`
	Location          string               `pulumi:"location"`
	Name              string               `pulumi:"name"`
	PeerNetworkCidrs  []string             `pulumi:"peerNetworkCidrs"`
	RemoteHost        string               `pulumi:"remoteHost"`
}

func LookupIpsecTunnelOutput(ctx *pulumi.Context, args LookupIpsecTunnelOutputArgs, opts ...pulumi.InvokeOption) LookupIpsecTunnelResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupIpsecTunnelResultOutput, error) {
			args := v.(LookupIpsecTunnelArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:vpn/getIpsecTunnel:getIpsecTunnel", args, LookupIpsecTunnelResultOutput{}, options).(LookupIpsecTunnelResultOutput), nil
		}).(LookupIpsecTunnelResultOutput)
}

// A collection of arguments for invoking getIpsecTunnel.
type LookupIpsecTunnelOutputArgs struct {
	GatewayId pulumi.StringInput    `pulumi:"gatewayId"`
	Id        pulumi.StringPtrInput `pulumi:"id"`
	Location  pulumi.StringInput    `pulumi:"location"`
	Name      pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupIpsecTunnelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpsecTunnelArgs)(nil)).Elem()
}

// A collection of values returned by getIpsecTunnel.
type LookupIpsecTunnelResultOutput struct{ *pulumi.OutputState }

func (LookupIpsecTunnelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpsecTunnelResult)(nil)).Elem()
}

func (o LookupIpsecTunnelResultOutput) ToLookupIpsecTunnelResultOutput() LookupIpsecTunnelResultOutput {
	return o
}

func (o LookupIpsecTunnelResultOutput) ToLookupIpsecTunnelResultOutputWithContext(ctx context.Context) LookupIpsecTunnelResultOutput {
	return o
}

func (o LookupIpsecTunnelResultOutput) Auths() GetIpsecTunnelAuthArrayOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) []GetIpsecTunnelAuth { return v.Auths }).(GetIpsecTunnelAuthArrayOutput)
}

func (o LookupIpsecTunnelResultOutput) CloudNetworkCidrs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) []string { return v.CloudNetworkCidrs }).(pulumi.StringArrayOutput)
}

func (o LookupIpsecTunnelResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupIpsecTunnelResultOutput) Esps() GetIpsecTunnelEspArrayOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) []GetIpsecTunnelEsp { return v.Esps }).(GetIpsecTunnelEspArrayOutput)
}

func (o LookupIpsecTunnelResultOutput) GatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) string { return v.GatewayId }).(pulumi.StringOutput)
}

func (o LookupIpsecTunnelResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupIpsecTunnelResultOutput) Ikes() GetIpsecTunnelIkeArrayOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) []GetIpsecTunnelIke { return v.Ikes }).(GetIpsecTunnelIkeArrayOutput)
}

func (o LookupIpsecTunnelResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) string { return v.Location }).(pulumi.StringOutput)
}

func (o LookupIpsecTunnelResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupIpsecTunnelResultOutput) PeerNetworkCidrs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) []string { return v.PeerNetworkCidrs }).(pulumi.StringArrayOutput)
}

func (o LookupIpsecTunnelResultOutput) RemoteHost() pulumi.StringOutput {
	return o.ApplyT(func(v LookupIpsecTunnelResult) string { return v.RemoteHost }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupIpsecTunnelResultOutput{})
}

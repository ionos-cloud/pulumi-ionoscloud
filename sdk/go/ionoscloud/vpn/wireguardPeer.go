// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpn

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This page provides an overview of the `vpn.WireguardPeer` resource, which allows you to manage a WireGuard Peer in your cloud infrastructure.
// This resource enables the creation, management, and deletion of a WireGuard VPN Peer, facilitating secure connections between your network resources.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/vpn"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := vpn.NewWireguardPeer(ctx, "example", &vpn.WireguardPeerArgs{
//				Location:    pulumi.String("de/fra"),
//				GatewayId:   pulumi.String("your gateway id here"),
//				Name:        pulumi.String("example-gateway"),
//				Description: pulumi.String("An example WireGuard peer"),
//				Endpoint: &vpn.WireguardPeerEndpointArgs{
//					Host: pulumi.String("1.2.3.4"),
//					Port: pulumi.Int(51820),
//				},
//				AllowedIps: pulumi.StringArray{
//					pulumi.String("10.0.0.0/8"),
//					pulumi.String("192.168.1.0/24"),
//				},
//				PublicKey: pulumi.String("examplePublicKey=="),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// WireGuard Peers can be imported using the `gateway_id` and `id`, e.g.,
//
// ```sh
// $ pulumi import ionoscloud:vpn/wireguardPeer:WireguardPeer example <gateway_id>:<peer_id>
// ```
type WireguardPeer struct {
	pulumi.CustomResourceState

	// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
	AllowedIps pulumi.StringArrayOutput `pulumi:"allowedIps"`
	// [string] A description of the WireGuard Gateway.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
	Endpoint WireguardPeerEndpointPtrOutput `pulumi:"endpoint"`
	// [string] The ID of the WireGuard Gateway that the Peer will connect to.
	GatewayId pulumi.StringOutput `pulumi:"gatewayId"`
	// [string] The location of the WireGuard Gateway.
	Location pulumi.StringOutput `pulumi:"location"`
	// [string] The human-readable name of the WireGuard Gateway.
	Name pulumi.StringOutput `pulumi:"name"`
	// [string] The public key for the WireGuard Gateway.
	PublicKey pulumi.StringOutput `pulumi:"publicKey"`
	// The current status of the WireGuard Gateway Peer.
	Status pulumi.StringOutput `pulumi:"status"`
}

// NewWireguardPeer registers a new resource with the given unique name, arguments, and options.
func NewWireguardPeer(ctx *pulumi.Context,
	name string, args *WireguardPeerArgs, opts ...pulumi.ResourceOption) (*WireguardPeer, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AllowedIps == nil {
		return nil, errors.New("invalid value for required argument 'AllowedIps'")
	}
	if args.GatewayId == nil {
		return nil, errors.New("invalid value for required argument 'GatewayId'")
	}
	if args.Location == nil {
		return nil, errors.New("invalid value for required argument 'Location'")
	}
	if args.PublicKey == nil {
		return nil, errors.New("invalid value for required argument 'PublicKey'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource WireguardPeer
	err := ctx.RegisterResource("ionoscloud:vpn/wireguardPeer:WireguardPeer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWireguardPeer gets an existing WireguardPeer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWireguardPeer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WireguardPeerState, opts ...pulumi.ResourceOption) (*WireguardPeer, error) {
	var resource WireguardPeer
	err := ctx.ReadResource("ionoscloud:vpn/wireguardPeer:WireguardPeer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WireguardPeer resources.
type wireguardPeerState struct {
	// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
	AllowedIps []string `pulumi:"allowedIps"`
	// [string] A description of the WireGuard Gateway.
	Description *string `pulumi:"description"`
	// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
	Endpoint *WireguardPeerEndpoint `pulumi:"endpoint"`
	// [string] The ID of the WireGuard Gateway that the Peer will connect to.
	GatewayId *string `pulumi:"gatewayId"`
	// [string] The location of the WireGuard Gateway.
	Location *string `pulumi:"location"`
	// [string] The human-readable name of the WireGuard Gateway.
	Name *string `pulumi:"name"`
	// [string] The public key for the WireGuard Gateway.
	PublicKey *string `pulumi:"publicKey"`
	// The current status of the WireGuard Gateway Peer.
	Status *string `pulumi:"status"`
}

type WireguardPeerState struct {
	// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
	AllowedIps pulumi.StringArrayInput
	// [string] A description of the WireGuard Gateway.
	Description pulumi.StringPtrInput
	// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
	Endpoint WireguardPeerEndpointPtrInput
	// [string] The ID of the WireGuard Gateway that the Peer will connect to.
	GatewayId pulumi.StringPtrInput
	// [string] The location of the WireGuard Gateway.
	Location pulumi.StringPtrInput
	// [string] The human-readable name of the WireGuard Gateway.
	Name pulumi.StringPtrInput
	// [string] The public key for the WireGuard Gateway.
	PublicKey pulumi.StringPtrInput
	// The current status of the WireGuard Gateway Peer.
	Status pulumi.StringPtrInput
}

func (WireguardPeerState) ElementType() reflect.Type {
	return reflect.TypeOf((*wireguardPeerState)(nil)).Elem()
}

type wireguardPeerArgs struct {
	// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
	AllowedIps []string `pulumi:"allowedIps"`
	// [string] A description of the WireGuard Gateway.
	Description *string `pulumi:"description"`
	// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
	Endpoint *WireguardPeerEndpoint `pulumi:"endpoint"`
	// [string] The ID of the WireGuard Gateway that the Peer will connect to.
	GatewayId string `pulumi:"gatewayId"`
	// [string] The location of the WireGuard Gateway.
	Location string `pulumi:"location"`
	// [string] The human-readable name of the WireGuard Gateway.
	Name *string `pulumi:"name"`
	// [string] The public key for the WireGuard Gateway.
	PublicKey string `pulumi:"publicKey"`
}

// The set of arguments for constructing a WireguardPeer resource.
type WireguardPeerArgs struct {
	// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
	AllowedIps pulumi.StringArrayInput
	// [string] A description of the WireGuard Gateway.
	Description pulumi.StringPtrInput
	// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
	Endpoint WireguardPeerEndpointPtrInput
	// [string] The ID of the WireGuard Gateway that the Peer will connect to.
	GatewayId pulumi.StringInput
	// [string] The location of the WireGuard Gateway.
	Location pulumi.StringInput
	// [string] The human-readable name of the WireGuard Gateway.
	Name pulumi.StringPtrInput
	// [string] The public key for the WireGuard Gateway.
	PublicKey pulumi.StringInput
}

func (WireguardPeerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*wireguardPeerArgs)(nil)).Elem()
}

type WireguardPeerInput interface {
	pulumi.Input

	ToWireguardPeerOutput() WireguardPeerOutput
	ToWireguardPeerOutputWithContext(ctx context.Context) WireguardPeerOutput
}

func (*WireguardPeer) ElementType() reflect.Type {
	return reflect.TypeOf((**WireguardPeer)(nil)).Elem()
}

func (i *WireguardPeer) ToWireguardPeerOutput() WireguardPeerOutput {
	return i.ToWireguardPeerOutputWithContext(context.Background())
}

func (i *WireguardPeer) ToWireguardPeerOutputWithContext(ctx context.Context) WireguardPeerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WireguardPeerOutput)
}

// WireguardPeerArrayInput is an input type that accepts WireguardPeerArray and WireguardPeerArrayOutput values.
// You can construct a concrete instance of `WireguardPeerArrayInput` via:
//
//	WireguardPeerArray{ WireguardPeerArgs{...} }
type WireguardPeerArrayInput interface {
	pulumi.Input

	ToWireguardPeerArrayOutput() WireguardPeerArrayOutput
	ToWireguardPeerArrayOutputWithContext(context.Context) WireguardPeerArrayOutput
}

type WireguardPeerArray []WireguardPeerInput

func (WireguardPeerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WireguardPeer)(nil)).Elem()
}

func (i WireguardPeerArray) ToWireguardPeerArrayOutput() WireguardPeerArrayOutput {
	return i.ToWireguardPeerArrayOutputWithContext(context.Background())
}

func (i WireguardPeerArray) ToWireguardPeerArrayOutputWithContext(ctx context.Context) WireguardPeerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WireguardPeerArrayOutput)
}

// WireguardPeerMapInput is an input type that accepts WireguardPeerMap and WireguardPeerMapOutput values.
// You can construct a concrete instance of `WireguardPeerMapInput` via:
//
//	WireguardPeerMap{ "key": WireguardPeerArgs{...} }
type WireguardPeerMapInput interface {
	pulumi.Input

	ToWireguardPeerMapOutput() WireguardPeerMapOutput
	ToWireguardPeerMapOutputWithContext(context.Context) WireguardPeerMapOutput
}

type WireguardPeerMap map[string]WireguardPeerInput

func (WireguardPeerMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WireguardPeer)(nil)).Elem()
}

func (i WireguardPeerMap) ToWireguardPeerMapOutput() WireguardPeerMapOutput {
	return i.ToWireguardPeerMapOutputWithContext(context.Background())
}

func (i WireguardPeerMap) ToWireguardPeerMapOutputWithContext(ctx context.Context) WireguardPeerMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WireguardPeerMapOutput)
}

type WireguardPeerOutput struct{ *pulumi.OutputState }

func (WireguardPeerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WireguardPeer)(nil)).Elem()
}

func (o WireguardPeerOutput) ToWireguardPeerOutput() WireguardPeerOutput {
	return o
}

func (o WireguardPeerOutput) ToWireguardPeerOutputWithContext(ctx context.Context) WireguardPeerOutput {
	return o
}

// [list, string] A list of subnet CIDRs that are allowed to connect to the WireGuard Gateway.
func (o WireguardPeerOutput) AllowedIps() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *WireguardPeer) pulumi.StringArrayOutput { return v.AllowedIps }).(pulumi.StringArrayOutput)
}

// [string] A description of the WireGuard Gateway.
func (o WireguardPeerOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *WireguardPeer) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// [block] An endpoint configuration block for the WireGuard Gateway. The structure of this block is as follows:
func (o WireguardPeerOutput) Endpoint() WireguardPeerEndpointPtrOutput {
	return o.ApplyT(func(v *WireguardPeer) WireguardPeerEndpointPtrOutput { return v.Endpoint }).(WireguardPeerEndpointPtrOutput)
}

// [string] The ID of the WireGuard Gateway that the Peer will connect to.
func (o WireguardPeerOutput) GatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v *WireguardPeer) pulumi.StringOutput { return v.GatewayId }).(pulumi.StringOutput)
}

// [string] The location of the WireGuard Gateway.
func (o WireguardPeerOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *WireguardPeer) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// [string] The human-readable name of the WireGuard Gateway.
func (o WireguardPeerOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *WireguardPeer) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [string] The public key for the WireGuard Gateway.
func (o WireguardPeerOutput) PublicKey() pulumi.StringOutput {
	return o.ApplyT(func(v *WireguardPeer) pulumi.StringOutput { return v.PublicKey }).(pulumi.StringOutput)
}

// The current status of the WireGuard Gateway Peer.
func (o WireguardPeerOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *WireguardPeer) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

type WireguardPeerArrayOutput struct{ *pulumi.OutputState }

func (WireguardPeerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WireguardPeer)(nil)).Elem()
}

func (o WireguardPeerArrayOutput) ToWireguardPeerArrayOutput() WireguardPeerArrayOutput {
	return o
}

func (o WireguardPeerArrayOutput) ToWireguardPeerArrayOutputWithContext(ctx context.Context) WireguardPeerArrayOutput {
	return o
}

func (o WireguardPeerArrayOutput) Index(i pulumi.IntInput) WireguardPeerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *WireguardPeer {
		return vs[0].([]*WireguardPeer)[vs[1].(int)]
	}).(WireguardPeerOutput)
}

type WireguardPeerMapOutput struct{ *pulumi.OutputState }

func (WireguardPeerMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WireguardPeer)(nil)).Elem()
}

func (o WireguardPeerMapOutput) ToWireguardPeerMapOutput() WireguardPeerMapOutput {
	return o
}

func (o WireguardPeerMapOutput) ToWireguardPeerMapOutputWithContext(ctx context.Context) WireguardPeerMapOutput {
	return o
}

func (o WireguardPeerMapOutput) MapIndex(k pulumi.StringInput) WireguardPeerOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *WireguardPeer {
		return vs[0].(map[string]*WireguardPeer)[vs[1].(string)]
	}).(WireguardPeerOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WireguardPeerInput)(nil)).Elem(), &WireguardPeer{})
	pulumi.RegisterInputType(reflect.TypeOf((*WireguardPeerArrayInput)(nil)).Elem(), WireguardPeerArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WireguardPeerMapInput)(nil)).Elem(), WireguardPeerMap{})
	pulumi.RegisterOutputType(WireguardPeerOutput{})
	pulumi.RegisterOutputType(WireguardPeerArrayOutput{})
	pulumi.RegisterOutputType(WireguardPeerMapOutput{})
}

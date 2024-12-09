// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Overview
//
// The `VpnWireguardGateway` resource manages a WireGuard Gateway within the IONOS Cloud infrastructure.
// This resource facilitates the creation, management, and deletion of WireGuard VPN Gateways, enabling secure connections between your network resources.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			datacenterExample, err := compute.NewDatacenter(ctx, "datacenterExample", &compute.DatacenterArgs{
//				Location: pulumi.String("de/fra"),
//			})
//			if err != nil {
//				return err
//			}
//			ipblockExample, err := compute.NewIPBlock(ctx, "ipblockExample", &compute.IPBlockArgs{
//				Location: pulumi.String("de/fra"),
//				Size:     pulumi.Int(1),
//			})
//			if err != nil {
//				return err
//			}
//			lanExample, err := compute.NewLan(ctx, "lanExample", &compute.LanArgs{
//				DatacenterId: datacenterExample.ID(),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ionoscloud.NewVpnWireguardGateway(ctx, "gateway", &ionoscloud.VpnWireguardGatewayArgs{
//				Location:    pulumi.String("de/fra"),
//				Description: pulumi.String("description"),
//				PrivateKey:  pulumi.String("private"),
//				GatewayIp: ipblockExample.Ips.ApplyT(func(ips []string) (string, error) {
//					return ips[0], nil
//				}).(pulumi.StringOutput),
//				InterfaceIpv4Cidr: pulumi.String("192.168.1.100/24"),
//				Connections: ionoscloud.VpnWireguardGatewayConnectionArray{
//					&ionoscloud.VpnWireguardGatewayConnectionArgs{
//						DatacenterId: datacenterExample.ID(),
//						LanId:        lanExample.ID(),
//						Ipv4Cidr:     pulumi.String("192.168.1.108/24"),
//					},
//				},
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
// WireGuard Gateways can be imported using their ID:
//
// ```sh
// $ pulumi import ionoscloud:index/vpnWireguardGateway:VpnWireguardGateway example_gateway location:id
// ```
type VpnWireguardGateway struct {
	pulumi.CustomResourceState

	// [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
	Connections VpnWireguardGatewayConnectionArrayOutput `pulumi:"connections"`
	// [String] A description of the WireGuard Gateway.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// [String] The IP address of the WireGuard Gateway.
	GatewayIp pulumi.StringOutput `pulumi:"gatewayIp"`
	// [String] The IPv4 CIDR for the WireGuard Gateway interface.
	InterfaceIpv4Cidr pulumi.StringPtrOutput `pulumi:"interfaceIpv4Cidr"`
	// [String] The IPv6 CIDR for the WireGuard Gateway interface.
	InterfaceIpv6Cidr pulumi.StringPtrOutput `pulumi:"interfaceIpv6Cidr"`
	ListenPort        pulumi.IntPtrOutput    `pulumi:"listenPort"`
	// [String] The location of the WireGuard Gateway.
	Location pulumi.StringOutput `pulumi:"location"`
	// [String] The name of the WireGuard Gateway.
	Name pulumi.StringOutput `pulumi:"name"`
	// [String] The private key for the WireGuard Gateway. To be created with the wg utility.
	PrivateKey pulumi.StringOutput `pulumi:"privateKey"`
	// (Computed)[String] The public key for the WireGuard Gateway.
	PublicKey pulumi.StringOutput `pulumi:"publicKey"`
	// (Computed)[String] The current status of the WireGuard Gateway.
	Status pulumi.StringOutput `pulumi:"status"`
}

// NewVpnWireguardGateway registers a new resource with the given unique name, arguments, and options.
func NewVpnWireguardGateway(ctx *pulumi.Context,
	name string, args *VpnWireguardGatewayArgs, opts ...pulumi.ResourceOption) (*VpnWireguardGateway, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Connections == nil {
		return nil, errors.New("invalid value for required argument 'Connections'")
	}
	if args.GatewayIp == nil {
		return nil, errors.New("invalid value for required argument 'GatewayIp'")
	}
	if args.Location == nil {
		return nil, errors.New("invalid value for required argument 'Location'")
	}
	if args.PrivateKey == nil {
		return nil, errors.New("invalid value for required argument 'PrivateKey'")
	}
	if args.PrivateKey != nil {
		args.PrivateKey = pulumi.ToSecret(args.PrivateKey).(pulumi.StringInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"privateKey",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VpnWireguardGateway
	err := ctx.RegisterResource("ionoscloud:index/vpnWireguardGateway:VpnWireguardGateway", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpnWireguardGateway gets an existing VpnWireguardGateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpnWireguardGateway(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpnWireguardGatewayState, opts ...pulumi.ResourceOption) (*VpnWireguardGateway, error) {
	var resource VpnWireguardGateway
	err := ctx.ReadResource("ionoscloud:index/vpnWireguardGateway:VpnWireguardGateway", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpnWireguardGateway resources.
type vpnWireguardGatewayState struct {
	// [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
	Connections []VpnWireguardGatewayConnection `pulumi:"connections"`
	// [String] A description of the WireGuard Gateway.
	Description *string `pulumi:"description"`
	// [String] The IP address of the WireGuard Gateway.
	GatewayIp *string `pulumi:"gatewayIp"`
	// [String] The IPv4 CIDR for the WireGuard Gateway interface.
	InterfaceIpv4Cidr *string `pulumi:"interfaceIpv4Cidr"`
	// [String] The IPv6 CIDR for the WireGuard Gateway interface.
	InterfaceIpv6Cidr *string `pulumi:"interfaceIpv6Cidr"`
	ListenPort        *int    `pulumi:"listenPort"`
	// [String] The location of the WireGuard Gateway.
	Location *string `pulumi:"location"`
	// [String] The name of the WireGuard Gateway.
	Name *string `pulumi:"name"`
	// [String] The private key for the WireGuard Gateway. To be created with the wg utility.
	PrivateKey *string `pulumi:"privateKey"`
	// (Computed)[String] The public key for the WireGuard Gateway.
	PublicKey *string `pulumi:"publicKey"`
	// (Computed)[String] The current status of the WireGuard Gateway.
	Status *string `pulumi:"status"`
}

type VpnWireguardGatewayState struct {
	// [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
	Connections VpnWireguardGatewayConnectionArrayInput
	// [String] A description of the WireGuard Gateway.
	Description pulumi.StringPtrInput
	// [String] The IP address of the WireGuard Gateway.
	GatewayIp pulumi.StringPtrInput
	// [String] The IPv4 CIDR for the WireGuard Gateway interface.
	InterfaceIpv4Cidr pulumi.StringPtrInput
	// [String] The IPv6 CIDR for the WireGuard Gateway interface.
	InterfaceIpv6Cidr pulumi.StringPtrInput
	ListenPort        pulumi.IntPtrInput
	// [String] The location of the WireGuard Gateway.
	Location pulumi.StringPtrInput
	// [String] The name of the WireGuard Gateway.
	Name pulumi.StringPtrInput
	// [String] The private key for the WireGuard Gateway. To be created with the wg utility.
	PrivateKey pulumi.StringPtrInput
	// (Computed)[String] The public key for the WireGuard Gateway.
	PublicKey pulumi.StringPtrInput
	// (Computed)[String] The current status of the WireGuard Gateway.
	Status pulumi.StringPtrInput
}

func (VpnWireguardGatewayState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpnWireguardGatewayState)(nil)).Elem()
}

type vpnWireguardGatewayArgs struct {
	// [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
	Connections []VpnWireguardGatewayConnection `pulumi:"connections"`
	// [String] A description of the WireGuard Gateway.
	Description *string `pulumi:"description"`
	// [String] The IP address of the WireGuard Gateway.
	GatewayIp string `pulumi:"gatewayIp"`
	// [String] The IPv4 CIDR for the WireGuard Gateway interface.
	InterfaceIpv4Cidr *string `pulumi:"interfaceIpv4Cidr"`
	// [String] The IPv6 CIDR for the WireGuard Gateway interface.
	InterfaceIpv6Cidr *string `pulumi:"interfaceIpv6Cidr"`
	ListenPort        *int    `pulumi:"listenPort"`
	// [String] The location of the WireGuard Gateway.
	Location string `pulumi:"location"`
	// [String] The name of the WireGuard Gateway.
	Name *string `pulumi:"name"`
	// [String] The private key for the WireGuard Gateway. To be created with the wg utility.
	PrivateKey string `pulumi:"privateKey"`
}

// The set of arguments for constructing a VpnWireguardGateway resource.
type VpnWireguardGatewayArgs struct {
	// [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
	Connections VpnWireguardGatewayConnectionArrayInput
	// [String] A description of the WireGuard Gateway.
	Description pulumi.StringPtrInput
	// [String] The IP address of the WireGuard Gateway.
	GatewayIp pulumi.StringInput
	// [String] The IPv4 CIDR for the WireGuard Gateway interface.
	InterfaceIpv4Cidr pulumi.StringPtrInput
	// [String] The IPv6 CIDR for the WireGuard Gateway interface.
	InterfaceIpv6Cidr pulumi.StringPtrInput
	ListenPort        pulumi.IntPtrInput
	// [String] The location of the WireGuard Gateway.
	Location pulumi.StringInput
	// [String] The name of the WireGuard Gateway.
	Name pulumi.StringPtrInput
	// [String] The private key for the WireGuard Gateway. To be created with the wg utility.
	PrivateKey pulumi.StringInput
}

func (VpnWireguardGatewayArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpnWireguardGatewayArgs)(nil)).Elem()
}

type VpnWireguardGatewayInput interface {
	pulumi.Input

	ToVpnWireguardGatewayOutput() VpnWireguardGatewayOutput
	ToVpnWireguardGatewayOutputWithContext(ctx context.Context) VpnWireguardGatewayOutput
}

func (*VpnWireguardGateway) ElementType() reflect.Type {
	return reflect.TypeOf((**VpnWireguardGateway)(nil)).Elem()
}

func (i *VpnWireguardGateway) ToVpnWireguardGatewayOutput() VpnWireguardGatewayOutput {
	return i.ToVpnWireguardGatewayOutputWithContext(context.Background())
}

func (i *VpnWireguardGateway) ToVpnWireguardGatewayOutputWithContext(ctx context.Context) VpnWireguardGatewayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpnWireguardGatewayOutput)
}

// VpnWireguardGatewayArrayInput is an input type that accepts VpnWireguardGatewayArray and VpnWireguardGatewayArrayOutput values.
// You can construct a concrete instance of `VpnWireguardGatewayArrayInput` via:
//
//	VpnWireguardGatewayArray{ VpnWireguardGatewayArgs{...} }
type VpnWireguardGatewayArrayInput interface {
	pulumi.Input

	ToVpnWireguardGatewayArrayOutput() VpnWireguardGatewayArrayOutput
	ToVpnWireguardGatewayArrayOutputWithContext(context.Context) VpnWireguardGatewayArrayOutput
}

type VpnWireguardGatewayArray []VpnWireguardGatewayInput

func (VpnWireguardGatewayArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VpnWireguardGateway)(nil)).Elem()
}

func (i VpnWireguardGatewayArray) ToVpnWireguardGatewayArrayOutput() VpnWireguardGatewayArrayOutput {
	return i.ToVpnWireguardGatewayArrayOutputWithContext(context.Background())
}

func (i VpnWireguardGatewayArray) ToVpnWireguardGatewayArrayOutputWithContext(ctx context.Context) VpnWireguardGatewayArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpnWireguardGatewayArrayOutput)
}

// VpnWireguardGatewayMapInput is an input type that accepts VpnWireguardGatewayMap and VpnWireguardGatewayMapOutput values.
// You can construct a concrete instance of `VpnWireguardGatewayMapInput` via:
//
//	VpnWireguardGatewayMap{ "key": VpnWireguardGatewayArgs{...} }
type VpnWireguardGatewayMapInput interface {
	pulumi.Input

	ToVpnWireguardGatewayMapOutput() VpnWireguardGatewayMapOutput
	ToVpnWireguardGatewayMapOutputWithContext(context.Context) VpnWireguardGatewayMapOutput
}

type VpnWireguardGatewayMap map[string]VpnWireguardGatewayInput

func (VpnWireguardGatewayMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VpnWireguardGateway)(nil)).Elem()
}

func (i VpnWireguardGatewayMap) ToVpnWireguardGatewayMapOutput() VpnWireguardGatewayMapOutput {
	return i.ToVpnWireguardGatewayMapOutputWithContext(context.Background())
}

func (i VpnWireguardGatewayMap) ToVpnWireguardGatewayMapOutputWithContext(ctx context.Context) VpnWireguardGatewayMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpnWireguardGatewayMapOutput)
}

type VpnWireguardGatewayOutput struct{ *pulumi.OutputState }

func (VpnWireguardGatewayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VpnWireguardGateway)(nil)).Elem()
}

func (o VpnWireguardGatewayOutput) ToVpnWireguardGatewayOutput() VpnWireguardGatewayOutput {
	return o
}

func (o VpnWireguardGatewayOutput) ToVpnWireguardGatewayOutputWithContext(ctx context.Context) VpnWireguardGatewayOutput {
	return o
}

// [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
func (o VpnWireguardGatewayOutput) Connections() VpnWireguardGatewayConnectionArrayOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) VpnWireguardGatewayConnectionArrayOutput { return v.Connections }).(VpnWireguardGatewayConnectionArrayOutput)
}

// [String] A description of the WireGuard Gateway.
func (o VpnWireguardGatewayOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// [String] The IP address of the WireGuard Gateway.
func (o VpnWireguardGatewayOutput) GatewayIp() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringOutput { return v.GatewayIp }).(pulumi.StringOutput)
}

// [String] The IPv4 CIDR for the WireGuard Gateway interface.
func (o VpnWireguardGatewayOutput) InterfaceIpv4Cidr() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringPtrOutput { return v.InterfaceIpv4Cidr }).(pulumi.StringPtrOutput)
}

// [String] The IPv6 CIDR for the WireGuard Gateway interface.
func (o VpnWireguardGatewayOutput) InterfaceIpv6Cidr() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringPtrOutput { return v.InterfaceIpv6Cidr }).(pulumi.StringPtrOutput)
}

func (o VpnWireguardGatewayOutput) ListenPort() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.IntPtrOutput { return v.ListenPort }).(pulumi.IntPtrOutput)
}

// [String] The location of the WireGuard Gateway.
func (o VpnWireguardGatewayOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// [String] The name of the WireGuard Gateway.
func (o VpnWireguardGatewayOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [String] The private key for the WireGuard Gateway. To be created with the wg utility.
func (o VpnWireguardGatewayOutput) PrivateKey() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringOutput { return v.PrivateKey }).(pulumi.StringOutput)
}

// (Computed)[String] The public key for the WireGuard Gateway.
func (o VpnWireguardGatewayOutput) PublicKey() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringOutput { return v.PublicKey }).(pulumi.StringOutput)
}

// (Computed)[String] The current status of the WireGuard Gateway.
func (o VpnWireguardGatewayOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnWireguardGateway) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

type VpnWireguardGatewayArrayOutput struct{ *pulumi.OutputState }

func (VpnWireguardGatewayArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*VpnWireguardGateway)(nil)).Elem()
}

func (o VpnWireguardGatewayArrayOutput) ToVpnWireguardGatewayArrayOutput() VpnWireguardGatewayArrayOutput {
	return o
}

func (o VpnWireguardGatewayArrayOutput) ToVpnWireguardGatewayArrayOutputWithContext(ctx context.Context) VpnWireguardGatewayArrayOutput {
	return o
}

func (o VpnWireguardGatewayArrayOutput) Index(i pulumi.IntInput) VpnWireguardGatewayOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *VpnWireguardGateway {
		return vs[0].([]*VpnWireguardGateway)[vs[1].(int)]
	}).(VpnWireguardGatewayOutput)
}

type VpnWireguardGatewayMapOutput struct{ *pulumi.OutputState }

func (VpnWireguardGatewayMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*VpnWireguardGateway)(nil)).Elem()
}

func (o VpnWireguardGatewayMapOutput) ToVpnWireguardGatewayMapOutput() VpnWireguardGatewayMapOutput {
	return o
}

func (o VpnWireguardGatewayMapOutput) ToVpnWireguardGatewayMapOutputWithContext(ctx context.Context) VpnWireguardGatewayMapOutput {
	return o
}

func (o VpnWireguardGatewayMapOutput) MapIndex(k pulumi.StringInput) VpnWireguardGatewayOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *VpnWireguardGateway {
		return vs[0].(map[string]*VpnWireguardGateway)[vs[1].(string)]
	}).(VpnWireguardGatewayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VpnWireguardGatewayInput)(nil)).Elem(), &VpnWireguardGateway{})
	pulumi.RegisterInputType(reflect.TypeOf((*VpnWireguardGatewayArrayInput)(nil)).Elem(), VpnWireguardGatewayArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VpnWireguardGatewayMapInput)(nil)).Elem(), VpnWireguardGatewayMap{})
	pulumi.RegisterOutputType(VpnWireguardGatewayOutput{})
	pulumi.RegisterOutputType(VpnWireguardGatewayArrayOutput{})
	pulumi.RegisterOutputType(VpnWireguardGatewayMapOutput{})
}

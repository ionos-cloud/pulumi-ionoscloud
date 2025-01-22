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

// An IPSec Gateway Tunnel resource manages the creation, management, and deletion of VPN IPSec Gateway Tunnels within the
// IONOS Cloud infrastructure. This resource facilitates the creation of VPN IPSec Gateway Tunnels, enabling secure
// connections between your network resources.
//
// ## Usage example
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/vpn"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			// Basic example
//			testDatacenter, err := compute.NewDatacenter(ctx, "test_datacenter", &compute.DatacenterArgs{
//				Name:     pulumi.String("test_vpn_gateway_basic"),
//				Location: pulumi.String("de/fra"),
//			})
//			if err != nil {
//				return err
//			}
//			testLan, err := compute.NewLan(ctx, "test_lan", &compute.LanArgs{
//				Name:         pulumi.String("test_lan_basic"),
//				Public:       pulumi.Bool(false),
//				DatacenterId: testDatacenter.ID(),
//			})
//			if err != nil {
//				return err
//			}
//			testIpblock, err := compute.NewIPBlock(ctx, "test_ipblock", &compute.IPBlockArgs{
//				Name:     pulumi.String("test_ipblock_basic"),
//				Location: pulumi.String("de/fra"),
//				Size:     pulumi.Int(1),
//			})
//			if err != nil {
//				return err
//			}
//			example, err := vpn.NewIpsecGateway(ctx, "example", &vpn.IpsecGatewayArgs{
//				Name:     pulumi.String("ipsec_gateway_basic"),
//				Location: pulumi.String("de/fra"),
//				GatewayIp: testIpblock.Ips.ApplyT(func(ips []string) (string, error) {
//					return ips[0], nil
//				}).(pulumi.StringOutput),
//				Version:     pulumi.String("IKEv2"),
//				Description: pulumi.String("This gateway connects site A to VDC X."),
//				Connections: vpn.IpsecGatewayConnectionArray{
//					&vpn.IpsecGatewayConnectionArgs{
//						DatacenterId: testDatacenter.ID(),
//						LanId:        testLan.ID(),
//						Ipv4Cidr:     pulumi.String("192.168.100.10/24"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = vpn.NewIpsecTunnel(ctx, "example", &vpn.IpsecTunnelArgs{
//				Location:    pulumi.String("de/fra"),
//				GatewayId:   example.ID(),
//				Name:        pulumi.String("example-tunnel"),
//				RemoteHost:  pulumi.String("vpn.mycompany.com"),
//				Description: pulumi.String("Allows local subnet X to connect to virtual network Y."),
//				Auth: &vpn.IpsecTunnelAuthArgs{
//					Method: pulumi.String("PSK"),
//					PskKey: pulumi.String("X2wosbaw74M8hQGbK3jCCaEusR6CCFRa"),
//				},
//				Ike: &vpn.IpsecTunnelIkeArgs{
//					DiffieHellmanGroup:  pulumi.String("16-MODP4096"),
//					EncryptionAlgorithm: pulumi.String("AES256"),
//					IntegrityAlgorithm:  pulumi.String("SHA256"),
//					Lifetime:            pulumi.Int(86400),
//				},
//				Esps: vpn.IpsecTunnelEspArray{
//					&vpn.IpsecTunnelEspArgs{
//						DiffieHellmanGroup:  pulumi.String("16-MODP4096"),
//						EncryptionAlgorithm: pulumi.String("AES256"),
//						IntegrityAlgorithm:  pulumi.String("SHA256"),
//						Lifetime:            pulumi.Int(3600),
//					},
//				},
//				CloudNetworkCidrs: pulumi.StringArray{
//					pulumi.String("0.0.0.0/0"),
//				},
//				PeerNetworkCidrs: pulumi.StringArray{
//					pulumi.String("1.2.3.4/32"),
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
// The resource can be imported using the `location`, `gateway_id` and `tunnel_id`, for example:
//
// ```sh
// $ pulumi import ionoscloud:vpn/ipsecTunnel:IpsecTunnel example location:gateway_id:tunnel_id
// ```
type IpsecTunnel struct {
	pulumi.CustomResourceState

	// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
	// items: 1.
	Auth IpsecTunnelAuthOutput `pulumi:"auth"`
	// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
	// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
	// Maximum items: 20.
	CloudNetworkCidrs pulumi.StringArrayOutput `pulumi:"cloudNetworkCidrs"`
	// [string] The human-readable description of your IPSec Gateway Tunnel.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
	Esps IpsecTunnelEspArrayOutput `pulumi:"esps"`
	// [string] The ID of the IPSec Gateway that the tunnel belongs to.
	GatewayId pulumi.StringOutput `pulumi:"gatewayId"`
	// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
	Ike IpsecTunnelIkeOutput `pulumi:"ike"`
	// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
	// gb/lhr, us/ewr, us/las, us/mci, fr/par
	Location pulumi.StringPtrOutput `pulumi:"location"`
	// [string] The name of the IPSec Gateway Tunnel.
	Name pulumi.StringOutput `pulumi:"name"`
	// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
	// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
	PeerNetworkCidrs pulumi.StringArrayOutput `pulumi:"peerNetworkCidrs"`
	// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
	RemoteHost pulumi.StringOutput `pulumi:"remoteHost"`
}

// NewIpsecTunnel registers a new resource with the given unique name, arguments, and options.
func NewIpsecTunnel(ctx *pulumi.Context,
	name string, args *IpsecTunnelArgs, opts ...pulumi.ResourceOption) (*IpsecTunnel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Auth == nil {
		return nil, errors.New("invalid value for required argument 'Auth'")
	}
	if args.CloudNetworkCidrs == nil {
		return nil, errors.New("invalid value for required argument 'CloudNetworkCidrs'")
	}
	if args.Esps == nil {
		return nil, errors.New("invalid value for required argument 'Esps'")
	}
	if args.GatewayId == nil {
		return nil, errors.New("invalid value for required argument 'GatewayId'")
	}
	if args.Ike == nil {
		return nil, errors.New("invalid value for required argument 'Ike'")
	}
	if args.PeerNetworkCidrs == nil {
		return nil, errors.New("invalid value for required argument 'PeerNetworkCidrs'")
	}
	if args.RemoteHost == nil {
		return nil, errors.New("invalid value for required argument 'RemoteHost'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource IpsecTunnel
	err := ctx.RegisterResource("ionoscloud:vpn/ipsecTunnel:IpsecTunnel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIpsecTunnel gets an existing IpsecTunnel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIpsecTunnel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IpsecTunnelState, opts ...pulumi.ResourceOption) (*IpsecTunnel, error) {
	var resource IpsecTunnel
	err := ctx.ReadResource("ionoscloud:vpn/ipsecTunnel:IpsecTunnel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IpsecTunnel resources.
type ipsecTunnelState struct {
	// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
	// items: 1.
	Auth *IpsecTunnelAuth `pulumi:"auth"`
	// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
	// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
	// Maximum items: 20.
	CloudNetworkCidrs []string `pulumi:"cloudNetworkCidrs"`
	// [string] The human-readable description of your IPSec Gateway Tunnel.
	Description *string `pulumi:"description"`
	// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
	Esps []IpsecTunnelEsp `pulumi:"esps"`
	// [string] The ID of the IPSec Gateway that the tunnel belongs to.
	GatewayId *string `pulumi:"gatewayId"`
	// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
	Ike *IpsecTunnelIke `pulumi:"ike"`
	// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
	// gb/lhr, us/ewr, us/las, us/mci, fr/par
	Location *string `pulumi:"location"`
	// [string] The name of the IPSec Gateway Tunnel.
	Name *string `pulumi:"name"`
	// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
	// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
	PeerNetworkCidrs []string `pulumi:"peerNetworkCidrs"`
	// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
	RemoteHost *string `pulumi:"remoteHost"`
}

type IpsecTunnelState struct {
	// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
	// items: 1.
	Auth IpsecTunnelAuthPtrInput
	// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
	// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
	// Maximum items: 20.
	CloudNetworkCidrs pulumi.StringArrayInput
	// [string] The human-readable description of your IPSec Gateway Tunnel.
	Description pulumi.StringPtrInput
	// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
	Esps IpsecTunnelEspArrayInput
	// [string] The ID of the IPSec Gateway that the tunnel belongs to.
	GatewayId pulumi.StringPtrInput
	// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
	Ike IpsecTunnelIkePtrInput
	// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
	// gb/lhr, us/ewr, us/las, us/mci, fr/par
	Location pulumi.StringPtrInput
	// [string] The name of the IPSec Gateway Tunnel.
	Name pulumi.StringPtrInput
	// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
	// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
	PeerNetworkCidrs pulumi.StringArrayInput
	// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
	RemoteHost pulumi.StringPtrInput
}

func (IpsecTunnelState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipsecTunnelState)(nil)).Elem()
}

type ipsecTunnelArgs struct {
	// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
	// items: 1.
	Auth IpsecTunnelAuth `pulumi:"auth"`
	// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
	// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
	// Maximum items: 20.
	CloudNetworkCidrs []string `pulumi:"cloudNetworkCidrs"`
	// [string] The human-readable description of your IPSec Gateway Tunnel.
	Description *string `pulumi:"description"`
	// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
	Esps []IpsecTunnelEsp `pulumi:"esps"`
	// [string] The ID of the IPSec Gateway that the tunnel belongs to.
	GatewayId string `pulumi:"gatewayId"`
	// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
	Ike IpsecTunnelIke `pulumi:"ike"`
	// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
	// gb/lhr, us/ewr, us/las, us/mci, fr/par
	Location *string `pulumi:"location"`
	// [string] The name of the IPSec Gateway Tunnel.
	Name *string `pulumi:"name"`
	// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
	// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
	PeerNetworkCidrs []string `pulumi:"peerNetworkCidrs"`
	// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
	RemoteHost string `pulumi:"remoteHost"`
}

// The set of arguments for constructing a IpsecTunnel resource.
type IpsecTunnelArgs struct {
	// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
	// items: 1.
	Auth IpsecTunnelAuthInput
	// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
	// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
	// Maximum items: 20.
	CloudNetworkCidrs pulumi.StringArrayInput
	// [string] The human-readable description of your IPSec Gateway Tunnel.
	Description pulumi.StringPtrInput
	// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
	Esps IpsecTunnelEspArrayInput
	// [string] The ID of the IPSec Gateway that the tunnel belongs to.
	GatewayId pulumi.StringInput
	// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
	Ike IpsecTunnelIkeInput
	// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
	// gb/lhr, us/ewr, us/las, us/mci, fr/par
	Location pulumi.StringPtrInput
	// [string] The name of the IPSec Gateway Tunnel.
	Name pulumi.StringPtrInput
	// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
	// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
	PeerNetworkCidrs pulumi.StringArrayInput
	// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
	RemoteHost pulumi.StringInput
}

func (IpsecTunnelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipsecTunnelArgs)(nil)).Elem()
}

type IpsecTunnelInput interface {
	pulumi.Input

	ToIpsecTunnelOutput() IpsecTunnelOutput
	ToIpsecTunnelOutputWithContext(ctx context.Context) IpsecTunnelOutput
}

func (*IpsecTunnel) ElementType() reflect.Type {
	return reflect.TypeOf((**IpsecTunnel)(nil)).Elem()
}

func (i *IpsecTunnel) ToIpsecTunnelOutput() IpsecTunnelOutput {
	return i.ToIpsecTunnelOutputWithContext(context.Background())
}

func (i *IpsecTunnel) ToIpsecTunnelOutputWithContext(ctx context.Context) IpsecTunnelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpsecTunnelOutput)
}

// IpsecTunnelArrayInput is an input type that accepts IpsecTunnelArray and IpsecTunnelArrayOutput values.
// You can construct a concrete instance of `IpsecTunnelArrayInput` via:
//
//	IpsecTunnelArray{ IpsecTunnelArgs{...} }
type IpsecTunnelArrayInput interface {
	pulumi.Input

	ToIpsecTunnelArrayOutput() IpsecTunnelArrayOutput
	ToIpsecTunnelArrayOutputWithContext(context.Context) IpsecTunnelArrayOutput
}

type IpsecTunnelArray []IpsecTunnelInput

func (IpsecTunnelArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IpsecTunnel)(nil)).Elem()
}

func (i IpsecTunnelArray) ToIpsecTunnelArrayOutput() IpsecTunnelArrayOutput {
	return i.ToIpsecTunnelArrayOutputWithContext(context.Background())
}

func (i IpsecTunnelArray) ToIpsecTunnelArrayOutputWithContext(ctx context.Context) IpsecTunnelArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpsecTunnelArrayOutput)
}

// IpsecTunnelMapInput is an input type that accepts IpsecTunnelMap and IpsecTunnelMapOutput values.
// You can construct a concrete instance of `IpsecTunnelMapInput` via:
//
//	IpsecTunnelMap{ "key": IpsecTunnelArgs{...} }
type IpsecTunnelMapInput interface {
	pulumi.Input

	ToIpsecTunnelMapOutput() IpsecTunnelMapOutput
	ToIpsecTunnelMapOutputWithContext(context.Context) IpsecTunnelMapOutput
}

type IpsecTunnelMap map[string]IpsecTunnelInput

func (IpsecTunnelMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IpsecTunnel)(nil)).Elem()
}

func (i IpsecTunnelMap) ToIpsecTunnelMapOutput() IpsecTunnelMapOutput {
	return i.ToIpsecTunnelMapOutputWithContext(context.Background())
}

func (i IpsecTunnelMap) ToIpsecTunnelMapOutputWithContext(ctx context.Context) IpsecTunnelMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpsecTunnelMapOutput)
}

type IpsecTunnelOutput struct{ *pulumi.OutputState }

func (IpsecTunnelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IpsecTunnel)(nil)).Elem()
}

func (o IpsecTunnelOutput) ToIpsecTunnelOutput() IpsecTunnelOutput {
	return o
}

func (o IpsecTunnelOutput) ToIpsecTunnelOutputWithContext(ctx context.Context) IpsecTunnelOutput {
	return o
}

// [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
// items: 1.
func (o IpsecTunnelOutput) Auth() IpsecTunnelAuthOutput {
	return o.ApplyT(func(v *IpsecTunnel) IpsecTunnelAuthOutput { return v.Auth }).(IpsecTunnelAuthOutput)
}

// [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
// tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
// Maximum items: 20.
func (o IpsecTunnelOutput) CloudNetworkCidrs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *IpsecTunnel) pulumi.StringArrayOutput { return v.CloudNetworkCidrs }).(pulumi.StringArrayOutput)
}

// [string] The human-readable description of your IPSec Gateway Tunnel.
func (o IpsecTunnelOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *IpsecTunnel) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
func (o IpsecTunnelOutput) Esps() IpsecTunnelEspArrayOutput {
	return o.ApplyT(func(v *IpsecTunnel) IpsecTunnelEspArrayOutput { return v.Esps }).(IpsecTunnelEspArrayOutput)
}

// [string] The ID of the IPSec Gateway that the tunnel belongs to.
func (o IpsecTunnelOutput) GatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v *IpsecTunnel) pulumi.StringOutput { return v.GatewayId }).(pulumi.StringOutput)
}

// [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
func (o IpsecTunnelOutput) Ike() IpsecTunnelIkeOutput {
	return o.ApplyT(func(v *IpsecTunnel) IpsecTunnelIkeOutput { return v.Ike }).(IpsecTunnelIkeOutput)
}

// [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
// gb/lhr, us/ewr, us/las, us/mci, fr/par
func (o IpsecTunnelOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *IpsecTunnel) pulumi.StringPtrOutput { return v.Location }).(pulumi.StringPtrOutput)
}

// [string] The name of the IPSec Gateway Tunnel.
func (o IpsecTunnelOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *IpsecTunnel) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
// tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
func (o IpsecTunnelOutput) PeerNetworkCidrs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *IpsecTunnel) pulumi.StringArrayOutput { return v.PeerNetworkCidrs }).(pulumi.StringArrayOutput)
}

// [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
func (o IpsecTunnelOutput) RemoteHost() pulumi.StringOutput {
	return o.ApplyT(func(v *IpsecTunnel) pulumi.StringOutput { return v.RemoteHost }).(pulumi.StringOutput)
}

type IpsecTunnelArrayOutput struct{ *pulumi.OutputState }

func (IpsecTunnelArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IpsecTunnel)(nil)).Elem()
}

func (o IpsecTunnelArrayOutput) ToIpsecTunnelArrayOutput() IpsecTunnelArrayOutput {
	return o
}

func (o IpsecTunnelArrayOutput) ToIpsecTunnelArrayOutputWithContext(ctx context.Context) IpsecTunnelArrayOutput {
	return o
}

func (o IpsecTunnelArrayOutput) Index(i pulumi.IntInput) IpsecTunnelOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *IpsecTunnel {
		return vs[0].([]*IpsecTunnel)[vs[1].(int)]
	}).(IpsecTunnelOutput)
}

type IpsecTunnelMapOutput struct{ *pulumi.OutputState }

func (IpsecTunnelMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IpsecTunnel)(nil)).Elem()
}

func (o IpsecTunnelMapOutput) ToIpsecTunnelMapOutput() IpsecTunnelMapOutput {
	return o
}

func (o IpsecTunnelMapOutput) ToIpsecTunnelMapOutputWithContext(ctx context.Context) IpsecTunnelMapOutput {
	return o
}

func (o IpsecTunnelMapOutput) MapIndex(k pulumi.StringInput) IpsecTunnelOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *IpsecTunnel {
		return vs[0].(map[string]*IpsecTunnel)[vs[1].(string)]
	}).(IpsecTunnelOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IpsecTunnelInput)(nil)).Elem(), &IpsecTunnel{})
	pulumi.RegisterInputType(reflect.TypeOf((*IpsecTunnelArrayInput)(nil)).Elem(), IpsecTunnelArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IpsecTunnelMapInput)(nil)).Elem(), IpsecTunnelMap{})
	pulumi.RegisterOutputType(IpsecTunnelOutput{})
	pulumi.RegisterOutputType(IpsecTunnelArrayOutput{})
	pulumi.RegisterOutputType(IpsecTunnelMapOutput{})
}

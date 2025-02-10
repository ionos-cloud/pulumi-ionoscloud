// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **Target Group** on IonosCloud.
//
// ## Example Usage
//
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
//			_, err := compute.NewTargetGroup(ctx, "example", &compute.TargetGroupArgs{
//				Name:            pulumi.String("Target Group Example"),
//				Algorithm:       pulumi.String("ROUND_ROBIN"),
//				Protocol:        pulumi.String("HTTP"),
//				ProtocolVersion: pulumi.String("HTTP1"),
//				Targets: compute.TargetGroupTargetArray{
//					&compute.TargetGroupTargetArgs{
//						Ip:                 pulumi.String("22.231.2.2"),
//						Port:               pulumi.Int(8080),
//						Weight:             pulumi.Int(1),
//						ProxyProtocol:      pulumi.String("v2ssl"),
//						HealthCheckEnabled: pulumi.Bool(true),
//						MaintenanceEnabled: pulumi.Bool(false),
//					},
//					&compute.TargetGroupTargetArgs{
//						Ip:                 pulumi.String("22.231.2.3"),
//						Port:               pulumi.Int(8081),
//						Weight:             pulumi.Int(124),
//						ProxyProtocol:      pulumi.String("v2"),
//						HealthCheckEnabled: pulumi.Bool(false),
//						MaintenanceEnabled: pulumi.Bool(false),
//					},
//				},
//				HealthCheck: &compute.TargetGroupHealthCheckArgs{
//					CheckTimeout:  pulumi.Int(5000),
//					CheckInterval: pulumi.Int(50000),
//					Retries:       pulumi.Int(2),
//				},
//				HttpHealthCheck: &compute.TargetGroupHttpHealthCheckArgs{
//					Path:      pulumi.String("/."),
//					Method:    pulumi.String("GET"),
//					MatchType: pulumi.String("STATUS_CODE"),
//					Response:  pulumi.String("200"),
//					Regex:     pulumi.Bool(true),
//					Negate:    pulumi.Bool(true),
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
// Resource Target Group can be imported using the `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:compute/targetGroup:TargetGroup myTargetGroup target group uuid
// ```
type TargetGroup struct {
	pulumi.CustomResourceState

	// [string] Balancing algorithm.
	Algorithm pulumi.StringOutput `pulumi:"algorithm"`
	// Health check attributes for Target Group.
	HealthCheck TargetGroupHealthCheckOutput `pulumi:"healthCheck"`
	// Http health check attributes for Target Group
	HttpHealthCheck TargetGroupHttpHealthCheckOutput `pulumi:"httpHealthCheck"`
	// [string] The name of the target group.
	Name pulumi.StringOutput `pulumi:"name"`
	// [string] Balancing protocol.
	Protocol pulumi.StringOutput `pulumi:"protocol"`
	// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
	ProtocolVersion pulumi.StringOutput `pulumi:"protocolVersion"`
	// [list] Array of items in the collection
	Targets TargetGroupTargetArrayOutput `pulumi:"targets"`
}

// NewTargetGroup registers a new resource with the given unique name, arguments, and options.
func NewTargetGroup(ctx *pulumi.Context,
	name string, args *TargetGroupArgs, opts ...pulumi.ResourceOption) (*TargetGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Algorithm == nil {
		return nil, errors.New("invalid value for required argument 'Algorithm'")
	}
	if args.Protocol == nil {
		return nil, errors.New("invalid value for required argument 'Protocol'")
	}
	if args.ProtocolVersion == nil {
		return nil, errors.New("invalid value for required argument 'ProtocolVersion'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TargetGroup
	err := ctx.RegisterResource("ionoscloud:compute/targetGroup:TargetGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTargetGroup gets an existing TargetGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTargetGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TargetGroupState, opts ...pulumi.ResourceOption) (*TargetGroup, error) {
	var resource TargetGroup
	err := ctx.ReadResource("ionoscloud:compute/targetGroup:TargetGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TargetGroup resources.
type targetGroupState struct {
	// [string] Balancing algorithm.
	Algorithm *string `pulumi:"algorithm"`
	// Health check attributes for Target Group.
	HealthCheck *TargetGroupHealthCheck `pulumi:"healthCheck"`
	// Http health check attributes for Target Group
	HttpHealthCheck *TargetGroupHttpHealthCheck `pulumi:"httpHealthCheck"`
	// [string] The name of the target group.
	Name *string `pulumi:"name"`
	// [string] Balancing protocol.
	Protocol *string `pulumi:"protocol"`
	// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
	ProtocolVersion *string `pulumi:"protocolVersion"`
	// [list] Array of items in the collection
	Targets []TargetGroupTarget `pulumi:"targets"`
}

type TargetGroupState struct {
	// [string] Balancing algorithm.
	Algorithm pulumi.StringPtrInput
	// Health check attributes for Target Group.
	HealthCheck TargetGroupHealthCheckPtrInput
	// Http health check attributes for Target Group
	HttpHealthCheck TargetGroupHttpHealthCheckPtrInput
	// [string] The name of the target group.
	Name pulumi.StringPtrInput
	// [string] Balancing protocol.
	Protocol pulumi.StringPtrInput
	// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
	ProtocolVersion pulumi.StringPtrInput
	// [list] Array of items in the collection
	Targets TargetGroupTargetArrayInput
}

func (TargetGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*targetGroupState)(nil)).Elem()
}

type targetGroupArgs struct {
	// [string] Balancing algorithm.
	Algorithm string `pulumi:"algorithm"`
	// Health check attributes for Target Group.
	HealthCheck *TargetGroupHealthCheck `pulumi:"healthCheck"`
	// Http health check attributes for Target Group
	HttpHealthCheck *TargetGroupHttpHealthCheck `pulumi:"httpHealthCheck"`
	// [string] The name of the target group.
	Name *string `pulumi:"name"`
	// [string] Balancing protocol.
	Protocol string `pulumi:"protocol"`
	// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
	ProtocolVersion string `pulumi:"protocolVersion"`
	// [list] Array of items in the collection
	Targets []TargetGroupTarget `pulumi:"targets"`
}

// The set of arguments for constructing a TargetGroup resource.
type TargetGroupArgs struct {
	// [string] Balancing algorithm.
	Algorithm pulumi.StringInput
	// Health check attributes for Target Group.
	HealthCheck TargetGroupHealthCheckPtrInput
	// Http health check attributes for Target Group
	HttpHealthCheck TargetGroupHttpHealthCheckPtrInput
	// [string] The name of the target group.
	Name pulumi.StringPtrInput
	// [string] Balancing protocol.
	Protocol pulumi.StringInput
	// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
	ProtocolVersion pulumi.StringInput
	// [list] Array of items in the collection
	Targets TargetGroupTargetArrayInput
}

func (TargetGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*targetGroupArgs)(nil)).Elem()
}

type TargetGroupInput interface {
	pulumi.Input

	ToTargetGroupOutput() TargetGroupOutput
	ToTargetGroupOutputWithContext(ctx context.Context) TargetGroupOutput
}

func (*TargetGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**TargetGroup)(nil)).Elem()
}

func (i *TargetGroup) ToTargetGroupOutput() TargetGroupOutput {
	return i.ToTargetGroupOutputWithContext(context.Background())
}

func (i *TargetGroup) ToTargetGroupOutputWithContext(ctx context.Context) TargetGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TargetGroupOutput)
}

// TargetGroupArrayInput is an input type that accepts TargetGroupArray and TargetGroupArrayOutput values.
// You can construct a concrete instance of `TargetGroupArrayInput` via:
//
//	TargetGroupArray{ TargetGroupArgs{...} }
type TargetGroupArrayInput interface {
	pulumi.Input

	ToTargetGroupArrayOutput() TargetGroupArrayOutput
	ToTargetGroupArrayOutputWithContext(context.Context) TargetGroupArrayOutput
}

type TargetGroupArray []TargetGroupInput

func (TargetGroupArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TargetGroup)(nil)).Elem()
}

func (i TargetGroupArray) ToTargetGroupArrayOutput() TargetGroupArrayOutput {
	return i.ToTargetGroupArrayOutputWithContext(context.Background())
}

func (i TargetGroupArray) ToTargetGroupArrayOutputWithContext(ctx context.Context) TargetGroupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TargetGroupArrayOutput)
}

// TargetGroupMapInput is an input type that accepts TargetGroupMap and TargetGroupMapOutput values.
// You can construct a concrete instance of `TargetGroupMapInput` via:
//
//	TargetGroupMap{ "key": TargetGroupArgs{...} }
type TargetGroupMapInput interface {
	pulumi.Input

	ToTargetGroupMapOutput() TargetGroupMapOutput
	ToTargetGroupMapOutputWithContext(context.Context) TargetGroupMapOutput
}

type TargetGroupMap map[string]TargetGroupInput

func (TargetGroupMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TargetGroup)(nil)).Elem()
}

func (i TargetGroupMap) ToTargetGroupMapOutput() TargetGroupMapOutput {
	return i.ToTargetGroupMapOutputWithContext(context.Background())
}

func (i TargetGroupMap) ToTargetGroupMapOutputWithContext(ctx context.Context) TargetGroupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TargetGroupMapOutput)
}

type TargetGroupOutput struct{ *pulumi.OutputState }

func (TargetGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TargetGroup)(nil)).Elem()
}

func (o TargetGroupOutput) ToTargetGroupOutput() TargetGroupOutput {
	return o
}

func (o TargetGroupOutput) ToTargetGroupOutputWithContext(ctx context.Context) TargetGroupOutput {
	return o
}

// [string] Balancing algorithm.
func (o TargetGroupOutput) Algorithm() pulumi.StringOutput {
	return o.ApplyT(func(v *TargetGroup) pulumi.StringOutput { return v.Algorithm }).(pulumi.StringOutput)
}

// Health check attributes for Target Group.
func (o TargetGroupOutput) HealthCheck() TargetGroupHealthCheckOutput {
	return o.ApplyT(func(v *TargetGroup) TargetGroupHealthCheckOutput { return v.HealthCheck }).(TargetGroupHealthCheckOutput)
}

// Http health check attributes for Target Group
func (o TargetGroupOutput) HttpHealthCheck() TargetGroupHttpHealthCheckOutput {
	return o.ApplyT(func(v *TargetGroup) TargetGroupHttpHealthCheckOutput { return v.HttpHealthCheck }).(TargetGroupHttpHealthCheckOutput)
}

// [string] The name of the target group.
func (o TargetGroupOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *TargetGroup) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [string] Balancing protocol.
func (o TargetGroupOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v *TargetGroup) pulumi.StringOutput { return v.Protocol }).(pulumi.StringOutput)
}

// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
func (o TargetGroupOutput) ProtocolVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *TargetGroup) pulumi.StringOutput { return v.ProtocolVersion }).(pulumi.StringOutput)
}

// [list] Array of items in the collection
func (o TargetGroupOutput) Targets() TargetGroupTargetArrayOutput {
	return o.ApplyT(func(v *TargetGroup) TargetGroupTargetArrayOutput { return v.Targets }).(TargetGroupTargetArrayOutput)
}

type TargetGroupArrayOutput struct{ *pulumi.OutputState }

func (TargetGroupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TargetGroup)(nil)).Elem()
}

func (o TargetGroupArrayOutput) ToTargetGroupArrayOutput() TargetGroupArrayOutput {
	return o
}

func (o TargetGroupArrayOutput) ToTargetGroupArrayOutputWithContext(ctx context.Context) TargetGroupArrayOutput {
	return o
}

func (o TargetGroupArrayOutput) Index(i pulumi.IntInput) TargetGroupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *TargetGroup {
		return vs[0].([]*TargetGroup)[vs[1].(int)]
	}).(TargetGroupOutput)
}

type TargetGroupMapOutput struct{ *pulumi.OutputState }

func (TargetGroupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TargetGroup)(nil)).Elem()
}

func (o TargetGroupMapOutput) ToTargetGroupMapOutput() TargetGroupMapOutput {
	return o
}

func (o TargetGroupMapOutput) ToTargetGroupMapOutputWithContext(ctx context.Context) TargetGroupMapOutput {
	return o
}

func (o TargetGroupMapOutput) MapIndex(k pulumi.StringInput) TargetGroupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *TargetGroup {
		return vs[0].(map[string]*TargetGroup)[vs[1].(string)]
	}).(TargetGroupOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TargetGroupInput)(nil)).Elem(), &TargetGroup{})
	pulumi.RegisterInputType(reflect.TypeOf((*TargetGroupArrayInput)(nil)).Elem(), TargetGroupArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TargetGroupMapInput)(nil)).Elem(), TargetGroupMap{})
	pulumi.RegisterOutputType(TargetGroupOutput{})
	pulumi.RegisterOutputType(TargetGroupArrayOutput{})
	pulumi.RegisterOutputType(TargetGroupMapOutput{})
}

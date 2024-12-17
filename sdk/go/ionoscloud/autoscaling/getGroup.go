// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package autoscaling

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The autoscaling group data source can be used to search for and return an existing Autoscaling Group. You can provide a string for the name or id parameters which will be compared with provisioned Autoscaling Groups. If a single match is found, it will be returned.
//
// ## Example Usage
//
// ### By Name
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/autoscaling"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := autoscaling.LookupGroup(ctx, &autoscaling.LookupGroupArgs{
//				Name: pulumi.StringRef("test_ds"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupGroup(ctx *pulumi.Context, args *LookupGroupArgs, opts ...pulumi.InvokeOption) (*LookupGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupGroupResult
	err := ctx.Invoke("ionoscloud:autoscaling/getGroup:getGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGroup.
type LookupGroupArgs struct {
	// Id of an existing Autoscaling Group that you want to search for.
	Id *string `pulumi:"id"`
	// Name of an existing Autoscaling Group that you want to search for.
	//
	// Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getGroup.
type LookupGroupResult struct {
	DatacenterId string `pulumi:"datacenterId"`
	// Unique identifier for the resource
	Id *string `pulumi:"id"`
	// Location of the datacenter. This location is the same as the one from the selected template.
	Location string `pulumi:"location"`
	// Maximum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
	MaxReplicaCount int `pulumi:"maxReplicaCount"`
	// Minimum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
	MinReplicaCount int `pulumi:"minReplicaCount"`
	// The name of the Autoscaling Group.
	Name *string `pulumi:"name"`
	// Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
	Policies              []GetGroupPolicy               `pulumi:"policies"`
	ReplicaConfigurations []GetGroupReplicaConfiguration `pulumi:"replicaConfigurations"`
	TargetReplicaCount    int                            `pulumi:"targetReplicaCount"`
}

func LookupGroupOutput(ctx *pulumi.Context, args LookupGroupOutputArgs, opts ...pulumi.InvokeOption) LookupGroupResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupGroupResultOutput, error) {
			args := v.(LookupGroupArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:autoscaling/getGroup:getGroup", args, LookupGroupResultOutput{}, options).(LookupGroupResultOutput), nil
		}).(LookupGroupResultOutput)
}

// A collection of arguments for invoking getGroup.
type LookupGroupOutputArgs struct {
	// Id of an existing Autoscaling Group that you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing Autoscaling Group that you want to search for.
	//
	// Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGroupArgs)(nil)).Elem()
}

// A collection of values returned by getGroup.
type LookupGroupResultOutput struct{ *pulumi.OutputState }

func (LookupGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGroupResult)(nil)).Elem()
}

func (o LookupGroupResultOutput) ToLookupGroupResultOutput() LookupGroupResultOutput {
	return o
}

func (o LookupGroupResultOutput) ToLookupGroupResultOutputWithContext(ctx context.Context) LookupGroupResultOutput {
	return o
}

func (o LookupGroupResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// Unique identifier for the resource
func (o LookupGroupResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGroupResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Location of the datacenter. This location is the same as the one from the selected template.
func (o LookupGroupResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGroupResult) string { return v.Location }).(pulumi.StringOutput)
}

// Maximum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
func (o LookupGroupResultOutput) MaxReplicaCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupGroupResult) int { return v.MaxReplicaCount }).(pulumi.IntOutput)
}

// Minimum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
func (o LookupGroupResultOutput) MinReplicaCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupGroupResult) int { return v.MinReplicaCount }).(pulumi.IntOutput)
}

// The name of the Autoscaling Group.
func (o LookupGroupResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGroupResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
func (o LookupGroupResultOutput) Policies() GetGroupPolicyArrayOutput {
	return o.ApplyT(func(v LookupGroupResult) []GetGroupPolicy { return v.Policies }).(GetGroupPolicyArrayOutput)
}

func (o LookupGroupResultOutput) ReplicaConfigurations() GetGroupReplicaConfigurationArrayOutput {
	return o.ApplyT(func(v LookupGroupResult) []GetGroupReplicaConfiguration { return v.ReplicaConfigurations }).(GetGroupReplicaConfigurationArrayOutput)
}

func (o LookupGroupResultOutput) TargetReplicaCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupGroupResult) int { return v.TargetReplicaCount }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGroupResultOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package monitoring

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **Monitoring pipeline**.
//
// > ⚠️  Only tokens are accepted for authorization in the **monitoring_pipeline** resource. Please ensure you are using tokens as other methods will not be valid.
//
// ## Usage example
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/monitoring"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := monitoring.NewPipeline(ctx, "example", &monitoring.PipelineArgs{
//				Location: pulumi.String("es/vit"),
//				Name:     pulumi.String("pipelineExample"),
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
// **NOTE:** The default timeout for all operations is 60 minutes. If you want to change the default value, you can use `timeouts` attribute inside the resource:
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/monitoring"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := monitoring.NewPipeline(ctx, "example", &monitoring.PipelineArgs{
//				Location: pulumi.String("es/vit"),
//				Name:     pulumi.String("pipelineExample"),
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
// In order to import a Monitoring pipeline, you can define an empty Monitoring pipeline resource in the plan:
//
// hcl
//
// resource "ionoscloud_monitoring_pipeline" "example" {
//
// }
//
// The resource can be imported using the `location` and `pipeline_id`, for example:
//
// ```sh
// $ pulumi import ionoscloud:monitoring/pipeline:Pipeline example location:pipeline_id
// ```
type Pipeline struct {
	pulumi.CustomResourceState

	// [string] The endpoint of the Grafana instance.
	GrafanaEndpoint pulumi.StringOutput `pulumi:"grafanaEndpoint"`
	// [string] The HTTP endpoint of the monitoring instance.
	HttpEndpoint pulumi.StringOutput `pulumi:"httpEndpoint"`
	// (Sensitive)[string] The key used to connect to the monitoring pipeline.
	//
	// > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
	Key pulumi.StringOutput `pulumi:"key"`
	// [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
	Location pulumi.StringPtrOutput `pulumi:"location"`
	// [string] The name of the Monitoring pipeline.
	Name     pulumi.StringOutput       `pulumi:"name"`
	Timeouts PipelineTimeoutsPtrOutput `pulumi:"timeouts"`
}

// NewPipeline registers a new resource with the given unique name, arguments, and options.
func NewPipeline(ctx *pulumi.Context,
	name string, args *PipelineArgs, opts ...pulumi.ResourceOption) (*Pipeline, error) {
	if args == nil {
		args = &PipelineArgs{}
	}

	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("ionoscloud:objectstorage/monitoringPipeline:MonitoringPipeline"),
		},
	})
	opts = append(opts, aliases)
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"key",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Pipeline
	err := ctx.RegisterResource("ionoscloud:monitoring/pipeline:Pipeline", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPipeline gets an existing Pipeline resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPipeline(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PipelineState, opts ...pulumi.ResourceOption) (*Pipeline, error) {
	var resource Pipeline
	err := ctx.ReadResource("ionoscloud:monitoring/pipeline:Pipeline", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Pipeline resources.
type pipelineState struct {
	// [string] The endpoint of the Grafana instance.
	GrafanaEndpoint *string `pulumi:"grafanaEndpoint"`
	// [string] The HTTP endpoint of the monitoring instance.
	HttpEndpoint *string `pulumi:"httpEndpoint"`
	// (Sensitive)[string] The key used to connect to the monitoring pipeline.
	//
	// > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
	Key *string `pulumi:"key"`
	// [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
	Location *string `pulumi:"location"`
	// [string] The name of the Monitoring pipeline.
	Name     *string           `pulumi:"name"`
	Timeouts *PipelineTimeouts `pulumi:"timeouts"`
}

type PipelineState struct {
	// [string] The endpoint of the Grafana instance.
	GrafanaEndpoint pulumi.StringPtrInput
	// [string] The HTTP endpoint of the monitoring instance.
	HttpEndpoint pulumi.StringPtrInput
	// (Sensitive)[string] The key used to connect to the monitoring pipeline.
	//
	// > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
	Key pulumi.StringPtrInput
	// [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
	Location pulumi.StringPtrInput
	// [string] The name of the Monitoring pipeline.
	Name     pulumi.StringPtrInput
	Timeouts PipelineTimeoutsPtrInput
}

func (PipelineState) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineState)(nil)).Elem()
}

type pipelineArgs struct {
	// [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
	Location *string `pulumi:"location"`
	// [string] The name of the Monitoring pipeline.
	Name     *string           `pulumi:"name"`
	Timeouts *PipelineTimeouts `pulumi:"timeouts"`
}

// The set of arguments for constructing a Pipeline resource.
type PipelineArgs struct {
	// [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
	Location pulumi.StringPtrInput
	// [string] The name of the Monitoring pipeline.
	Name     pulumi.StringPtrInput
	Timeouts PipelineTimeoutsPtrInput
}

func (PipelineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineArgs)(nil)).Elem()
}

type PipelineInput interface {
	pulumi.Input

	ToPipelineOutput() PipelineOutput
	ToPipelineOutputWithContext(ctx context.Context) PipelineOutput
}

func (*Pipeline) ElementType() reflect.Type {
	return reflect.TypeOf((**Pipeline)(nil)).Elem()
}

func (i *Pipeline) ToPipelineOutput() PipelineOutput {
	return i.ToPipelineOutputWithContext(context.Background())
}

func (i *Pipeline) ToPipelineOutputWithContext(ctx context.Context) PipelineOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineOutput)
}

// PipelineArrayInput is an input type that accepts PipelineArray and PipelineArrayOutput values.
// You can construct a concrete instance of `PipelineArrayInput` via:
//
//	PipelineArray{ PipelineArgs{...} }
type PipelineArrayInput interface {
	pulumi.Input

	ToPipelineArrayOutput() PipelineArrayOutput
	ToPipelineArrayOutputWithContext(context.Context) PipelineArrayOutput
}

type PipelineArray []PipelineInput

func (PipelineArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Pipeline)(nil)).Elem()
}

func (i PipelineArray) ToPipelineArrayOutput() PipelineArrayOutput {
	return i.ToPipelineArrayOutputWithContext(context.Background())
}

func (i PipelineArray) ToPipelineArrayOutputWithContext(ctx context.Context) PipelineArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineArrayOutput)
}

// PipelineMapInput is an input type that accepts PipelineMap and PipelineMapOutput values.
// You can construct a concrete instance of `PipelineMapInput` via:
//
//	PipelineMap{ "key": PipelineArgs{...} }
type PipelineMapInput interface {
	pulumi.Input

	ToPipelineMapOutput() PipelineMapOutput
	ToPipelineMapOutputWithContext(context.Context) PipelineMapOutput
}

type PipelineMap map[string]PipelineInput

func (PipelineMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Pipeline)(nil)).Elem()
}

func (i PipelineMap) ToPipelineMapOutput() PipelineMapOutput {
	return i.ToPipelineMapOutputWithContext(context.Background())
}

func (i PipelineMap) ToPipelineMapOutputWithContext(ctx context.Context) PipelineMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineMapOutput)
}

type PipelineOutput struct{ *pulumi.OutputState }

func (PipelineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Pipeline)(nil)).Elem()
}

func (o PipelineOutput) ToPipelineOutput() PipelineOutput {
	return o
}

func (o PipelineOutput) ToPipelineOutputWithContext(ctx context.Context) PipelineOutput {
	return o
}

// [string] The endpoint of the Grafana instance.
func (o PipelineOutput) GrafanaEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringOutput { return v.GrafanaEndpoint }).(pulumi.StringOutput)
}

// [string] The HTTP endpoint of the monitoring instance.
func (o PipelineOutput) HttpEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringOutput { return v.HttpEndpoint }).(pulumi.StringOutput)
}

// (Sensitive)[string] The key used to connect to the monitoring pipeline.
//
// > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
func (o PipelineOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

// [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
func (o PipelineOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringPtrOutput { return v.Location }).(pulumi.StringPtrOutput)
}

// [string] The name of the Monitoring pipeline.
func (o PipelineOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Pipeline) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o PipelineOutput) Timeouts() PipelineTimeoutsPtrOutput {
	return o.ApplyT(func(v *Pipeline) PipelineTimeoutsPtrOutput { return v.Timeouts }).(PipelineTimeoutsPtrOutput)
}

type PipelineArrayOutput struct{ *pulumi.OutputState }

func (PipelineArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Pipeline)(nil)).Elem()
}

func (o PipelineArrayOutput) ToPipelineArrayOutput() PipelineArrayOutput {
	return o
}

func (o PipelineArrayOutput) ToPipelineArrayOutputWithContext(ctx context.Context) PipelineArrayOutput {
	return o
}

func (o PipelineArrayOutput) Index(i pulumi.IntInput) PipelineOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Pipeline {
		return vs[0].([]*Pipeline)[vs[1].(int)]
	}).(PipelineOutput)
}

type PipelineMapOutput struct{ *pulumi.OutputState }

func (PipelineMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Pipeline)(nil)).Elem()
}

func (o PipelineMapOutput) ToPipelineMapOutput() PipelineMapOutput {
	return o
}

func (o PipelineMapOutput) ToPipelineMapOutputWithContext(ctx context.Context) PipelineMapOutput {
	return o
}

func (o PipelineMapOutput) MapIndex(k pulumi.StringInput) PipelineOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Pipeline {
		return vs[0].(map[string]*Pipeline)[vs[1].(string)]
	}).(PipelineOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineInput)(nil)).Elem(), &Pipeline{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineArrayInput)(nil)).Elem(), PipelineArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineMapInput)(nil)).Elem(), PipelineMap{})
	pulumi.RegisterOutputType(PipelineOutput{})
	pulumi.RegisterOutputType(PipelineArrayOutput{})
	pulumi.RegisterOutputType(PipelineMapOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package logging

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type PipelineLog struct {
	// [list] The configuration of the logs datastore, a list that contains elements with the following structure:
	Destinations []PipelineLogDestination `pulumi:"destinations"`
	// [string] "Protocol to use as intake. Possible values are: http, tcp."
	Protocol string `pulumi:"protocol"`
	// [bool]
	Public *bool `pulumi:"public"`
	// [string] The source parser to be used.
	Source string `pulumi:"source"`
	// [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
	Tag string `pulumi:"tag"`
}

// PipelineLogInput is an input type that accepts PipelineLogArgs and PipelineLogOutput values.
// You can construct a concrete instance of `PipelineLogInput` via:
//
//	PipelineLogArgs{...}
type PipelineLogInput interface {
	pulumi.Input

	ToPipelineLogOutput() PipelineLogOutput
	ToPipelineLogOutputWithContext(context.Context) PipelineLogOutput
}

type PipelineLogArgs struct {
	// [list] The configuration of the logs datastore, a list that contains elements with the following structure:
	Destinations PipelineLogDestinationArrayInput `pulumi:"destinations"`
	// [string] "Protocol to use as intake. Possible values are: http, tcp."
	Protocol pulumi.StringInput `pulumi:"protocol"`
	// [bool]
	Public pulumi.BoolPtrInput `pulumi:"public"`
	// [string] The source parser to be used.
	Source pulumi.StringInput `pulumi:"source"`
	// [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
	Tag pulumi.StringInput `pulumi:"tag"`
}

func (PipelineLogArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PipelineLog)(nil)).Elem()
}

func (i PipelineLogArgs) ToPipelineLogOutput() PipelineLogOutput {
	return i.ToPipelineLogOutputWithContext(context.Background())
}

func (i PipelineLogArgs) ToPipelineLogOutputWithContext(ctx context.Context) PipelineLogOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineLogOutput)
}

// PipelineLogArrayInput is an input type that accepts PipelineLogArray and PipelineLogArrayOutput values.
// You can construct a concrete instance of `PipelineLogArrayInput` via:
//
//	PipelineLogArray{ PipelineLogArgs{...} }
type PipelineLogArrayInput interface {
	pulumi.Input

	ToPipelineLogArrayOutput() PipelineLogArrayOutput
	ToPipelineLogArrayOutputWithContext(context.Context) PipelineLogArrayOutput
}

type PipelineLogArray []PipelineLogInput

func (PipelineLogArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PipelineLog)(nil)).Elem()
}

func (i PipelineLogArray) ToPipelineLogArrayOutput() PipelineLogArrayOutput {
	return i.ToPipelineLogArrayOutputWithContext(context.Background())
}

func (i PipelineLogArray) ToPipelineLogArrayOutputWithContext(ctx context.Context) PipelineLogArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineLogArrayOutput)
}

type PipelineLogOutput struct{ *pulumi.OutputState }

func (PipelineLogOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PipelineLog)(nil)).Elem()
}

func (o PipelineLogOutput) ToPipelineLogOutput() PipelineLogOutput {
	return o
}

func (o PipelineLogOutput) ToPipelineLogOutputWithContext(ctx context.Context) PipelineLogOutput {
	return o
}

// [list] The configuration of the logs datastore, a list that contains elements with the following structure:
func (o PipelineLogOutput) Destinations() PipelineLogDestinationArrayOutput {
	return o.ApplyT(func(v PipelineLog) []PipelineLogDestination { return v.Destinations }).(PipelineLogDestinationArrayOutput)
}

// [string] "Protocol to use as intake. Possible values are: http, tcp."
func (o PipelineLogOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v PipelineLog) string { return v.Protocol }).(pulumi.StringOutput)
}

// [bool]
func (o PipelineLogOutput) Public() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v PipelineLog) *bool { return v.Public }).(pulumi.BoolPtrOutput)
}

// [string] The source parser to be used.
func (o PipelineLogOutput) Source() pulumi.StringOutput {
	return o.ApplyT(func(v PipelineLog) string { return v.Source }).(pulumi.StringOutput)
}

// [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
func (o PipelineLogOutput) Tag() pulumi.StringOutput {
	return o.ApplyT(func(v PipelineLog) string { return v.Tag }).(pulumi.StringOutput)
}

type PipelineLogArrayOutput struct{ *pulumi.OutputState }

func (PipelineLogArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PipelineLog)(nil)).Elem()
}

func (o PipelineLogArrayOutput) ToPipelineLogArrayOutput() PipelineLogArrayOutput {
	return o
}

func (o PipelineLogArrayOutput) ToPipelineLogArrayOutputWithContext(ctx context.Context) PipelineLogArrayOutput {
	return o
}

func (o PipelineLogArrayOutput) Index(i pulumi.IntInput) PipelineLogOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) PipelineLog {
		return vs[0].([]PipelineLog)[vs[1].(int)]
	}).(PipelineLogOutput)
}

type PipelineLogDestination struct {
	// [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
	RetentionInDays *int `pulumi:"retentionInDays"`
	// [string] The internal output stream to send logs to.
	Type *string `pulumi:"type"`
}

// PipelineLogDestinationInput is an input type that accepts PipelineLogDestinationArgs and PipelineLogDestinationOutput values.
// You can construct a concrete instance of `PipelineLogDestinationInput` via:
//
//	PipelineLogDestinationArgs{...}
type PipelineLogDestinationInput interface {
	pulumi.Input

	ToPipelineLogDestinationOutput() PipelineLogDestinationOutput
	ToPipelineLogDestinationOutputWithContext(context.Context) PipelineLogDestinationOutput
}

type PipelineLogDestinationArgs struct {
	// [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
	RetentionInDays pulumi.IntPtrInput `pulumi:"retentionInDays"`
	// [string] The internal output stream to send logs to.
	Type pulumi.StringPtrInput `pulumi:"type"`
}

func (PipelineLogDestinationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*PipelineLogDestination)(nil)).Elem()
}

func (i PipelineLogDestinationArgs) ToPipelineLogDestinationOutput() PipelineLogDestinationOutput {
	return i.ToPipelineLogDestinationOutputWithContext(context.Background())
}

func (i PipelineLogDestinationArgs) ToPipelineLogDestinationOutputWithContext(ctx context.Context) PipelineLogDestinationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineLogDestinationOutput)
}

// PipelineLogDestinationArrayInput is an input type that accepts PipelineLogDestinationArray and PipelineLogDestinationArrayOutput values.
// You can construct a concrete instance of `PipelineLogDestinationArrayInput` via:
//
//	PipelineLogDestinationArray{ PipelineLogDestinationArgs{...} }
type PipelineLogDestinationArrayInput interface {
	pulumi.Input

	ToPipelineLogDestinationArrayOutput() PipelineLogDestinationArrayOutput
	ToPipelineLogDestinationArrayOutputWithContext(context.Context) PipelineLogDestinationArrayOutput
}

type PipelineLogDestinationArray []PipelineLogDestinationInput

func (PipelineLogDestinationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PipelineLogDestination)(nil)).Elem()
}

func (i PipelineLogDestinationArray) ToPipelineLogDestinationArrayOutput() PipelineLogDestinationArrayOutput {
	return i.ToPipelineLogDestinationArrayOutputWithContext(context.Background())
}

func (i PipelineLogDestinationArray) ToPipelineLogDestinationArrayOutputWithContext(ctx context.Context) PipelineLogDestinationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineLogDestinationArrayOutput)
}

type PipelineLogDestinationOutput struct{ *pulumi.OutputState }

func (PipelineLogDestinationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PipelineLogDestination)(nil)).Elem()
}

func (o PipelineLogDestinationOutput) ToPipelineLogDestinationOutput() PipelineLogDestinationOutput {
	return o
}

func (o PipelineLogDestinationOutput) ToPipelineLogDestinationOutputWithContext(ctx context.Context) PipelineLogDestinationOutput {
	return o
}

// [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
func (o PipelineLogDestinationOutput) RetentionInDays() pulumi.IntPtrOutput {
	return o.ApplyT(func(v PipelineLogDestination) *int { return v.RetentionInDays }).(pulumi.IntPtrOutput)
}

// [string] The internal output stream to send logs to.
func (o PipelineLogDestinationOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v PipelineLogDestination) *string { return v.Type }).(pulumi.StringPtrOutput)
}

type PipelineLogDestinationArrayOutput struct{ *pulumi.OutputState }

func (PipelineLogDestinationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PipelineLogDestination)(nil)).Elem()
}

func (o PipelineLogDestinationArrayOutput) ToPipelineLogDestinationArrayOutput() PipelineLogDestinationArrayOutput {
	return o
}

func (o PipelineLogDestinationArrayOutput) ToPipelineLogDestinationArrayOutputWithContext(ctx context.Context) PipelineLogDestinationArrayOutput {
	return o
}

func (o PipelineLogDestinationArrayOutput) Index(i pulumi.IntInput) PipelineLogDestinationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) PipelineLogDestination {
		return vs[0].([]PipelineLogDestination)[vs[1].(int)]
	}).(PipelineLogDestinationOutput)
}

type GetPipelineLog struct {
	// [list] The configuration of the logs datastore, a list that contains elements with the following structure:
	Destinations []GetPipelineLogDestination `pulumi:"destinations"`
	// [string] "Protocol to use as intake. Possible values are: http, tcp."
	Protocol string `pulumi:"protocol"`
	// [bool]
	Public bool `pulumi:"public"`
	// [string] The source parser to be used.
	Source string `pulumi:"source"`
	// [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
	Tag string `pulumi:"tag"`
}

// GetPipelineLogInput is an input type that accepts GetPipelineLogArgs and GetPipelineLogOutput values.
// You can construct a concrete instance of `GetPipelineLogInput` via:
//
//	GetPipelineLogArgs{...}
type GetPipelineLogInput interface {
	pulumi.Input

	ToGetPipelineLogOutput() GetPipelineLogOutput
	ToGetPipelineLogOutputWithContext(context.Context) GetPipelineLogOutput
}

type GetPipelineLogArgs struct {
	// [list] The configuration of the logs datastore, a list that contains elements with the following structure:
	Destinations GetPipelineLogDestinationArrayInput `pulumi:"destinations"`
	// [string] "Protocol to use as intake. Possible values are: http, tcp."
	Protocol pulumi.StringInput `pulumi:"protocol"`
	// [bool]
	Public pulumi.BoolInput `pulumi:"public"`
	// [string] The source parser to be used.
	Source pulumi.StringInput `pulumi:"source"`
	// [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
	Tag pulumi.StringInput `pulumi:"tag"`
}

func (GetPipelineLogArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPipelineLog)(nil)).Elem()
}

func (i GetPipelineLogArgs) ToGetPipelineLogOutput() GetPipelineLogOutput {
	return i.ToGetPipelineLogOutputWithContext(context.Background())
}

func (i GetPipelineLogArgs) ToGetPipelineLogOutputWithContext(ctx context.Context) GetPipelineLogOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetPipelineLogOutput)
}

// GetPipelineLogArrayInput is an input type that accepts GetPipelineLogArray and GetPipelineLogArrayOutput values.
// You can construct a concrete instance of `GetPipelineLogArrayInput` via:
//
//	GetPipelineLogArray{ GetPipelineLogArgs{...} }
type GetPipelineLogArrayInput interface {
	pulumi.Input

	ToGetPipelineLogArrayOutput() GetPipelineLogArrayOutput
	ToGetPipelineLogArrayOutputWithContext(context.Context) GetPipelineLogArrayOutput
}

type GetPipelineLogArray []GetPipelineLogInput

func (GetPipelineLogArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetPipelineLog)(nil)).Elem()
}

func (i GetPipelineLogArray) ToGetPipelineLogArrayOutput() GetPipelineLogArrayOutput {
	return i.ToGetPipelineLogArrayOutputWithContext(context.Background())
}

func (i GetPipelineLogArray) ToGetPipelineLogArrayOutputWithContext(ctx context.Context) GetPipelineLogArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetPipelineLogArrayOutput)
}

type GetPipelineLogOutput struct{ *pulumi.OutputState }

func (GetPipelineLogOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPipelineLog)(nil)).Elem()
}

func (o GetPipelineLogOutput) ToGetPipelineLogOutput() GetPipelineLogOutput {
	return o
}

func (o GetPipelineLogOutput) ToGetPipelineLogOutputWithContext(ctx context.Context) GetPipelineLogOutput {
	return o
}

// [list] The configuration of the logs datastore, a list that contains elements with the following structure:
func (o GetPipelineLogOutput) Destinations() GetPipelineLogDestinationArrayOutput {
	return o.ApplyT(func(v GetPipelineLog) []GetPipelineLogDestination { return v.Destinations }).(GetPipelineLogDestinationArrayOutput)
}

// [string] "Protocol to use as intake. Possible values are: http, tcp."
func (o GetPipelineLogOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v GetPipelineLog) string { return v.Protocol }).(pulumi.StringOutput)
}

// [bool]
func (o GetPipelineLogOutput) Public() pulumi.BoolOutput {
	return o.ApplyT(func(v GetPipelineLog) bool { return v.Public }).(pulumi.BoolOutput)
}

// [string] The source parser to be used.
func (o GetPipelineLogOutput) Source() pulumi.StringOutput {
	return o.ApplyT(func(v GetPipelineLog) string { return v.Source }).(pulumi.StringOutput)
}

// [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
func (o GetPipelineLogOutput) Tag() pulumi.StringOutput {
	return o.ApplyT(func(v GetPipelineLog) string { return v.Tag }).(pulumi.StringOutput)
}

type GetPipelineLogArrayOutput struct{ *pulumi.OutputState }

func (GetPipelineLogArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetPipelineLog)(nil)).Elem()
}

func (o GetPipelineLogArrayOutput) ToGetPipelineLogArrayOutput() GetPipelineLogArrayOutput {
	return o
}

func (o GetPipelineLogArrayOutput) ToGetPipelineLogArrayOutputWithContext(ctx context.Context) GetPipelineLogArrayOutput {
	return o
}

func (o GetPipelineLogArrayOutput) Index(i pulumi.IntInput) GetPipelineLogOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetPipelineLog {
		return vs[0].([]GetPipelineLog)[vs[1].(int)]
	}).(GetPipelineLogOutput)
}

type GetPipelineLogDestination struct {
	// [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only.
	RetentionInDays int `pulumi:"retentionInDays"`
	// [string] The internal output stream to send logs to.
	Type string `pulumi:"type"`
}

// GetPipelineLogDestinationInput is an input type that accepts GetPipelineLogDestinationArgs and GetPipelineLogDestinationOutput values.
// You can construct a concrete instance of `GetPipelineLogDestinationInput` via:
//
//	GetPipelineLogDestinationArgs{...}
type GetPipelineLogDestinationInput interface {
	pulumi.Input

	ToGetPipelineLogDestinationOutput() GetPipelineLogDestinationOutput
	ToGetPipelineLogDestinationOutputWithContext(context.Context) GetPipelineLogDestinationOutput
}

type GetPipelineLogDestinationArgs struct {
	// [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only.
	RetentionInDays pulumi.IntInput `pulumi:"retentionInDays"`
	// [string] The internal output stream to send logs to.
	Type pulumi.StringInput `pulumi:"type"`
}

func (GetPipelineLogDestinationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPipelineLogDestination)(nil)).Elem()
}

func (i GetPipelineLogDestinationArgs) ToGetPipelineLogDestinationOutput() GetPipelineLogDestinationOutput {
	return i.ToGetPipelineLogDestinationOutputWithContext(context.Background())
}

func (i GetPipelineLogDestinationArgs) ToGetPipelineLogDestinationOutputWithContext(ctx context.Context) GetPipelineLogDestinationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetPipelineLogDestinationOutput)
}

// GetPipelineLogDestinationArrayInput is an input type that accepts GetPipelineLogDestinationArray and GetPipelineLogDestinationArrayOutput values.
// You can construct a concrete instance of `GetPipelineLogDestinationArrayInput` via:
//
//	GetPipelineLogDestinationArray{ GetPipelineLogDestinationArgs{...} }
type GetPipelineLogDestinationArrayInput interface {
	pulumi.Input

	ToGetPipelineLogDestinationArrayOutput() GetPipelineLogDestinationArrayOutput
	ToGetPipelineLogDestinationArrayOutputWithContext(context.Context) GetPipelineLogDestinationArrayOutput
}

type GetPipelineLogDestinationArray []GetPipelineLogDestinationInput

func (GetPipelineLogDestinationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetPipelineLogDestination)(nil)).Elem()
}

func (i GetPipelineLogDestinationArray) ToGetPipelineLogDestinationArrayOutput() GetPipelineLogDestinationArrayOutput {
	return i.ToGetPipelineLogDestinationArrayOutputWithContext(context.Background())
}

func (i GetPipelineLogDestinationArray) ToGetPipelineLogDestinationArrayOutputWithContext(ctx context.Context) GetPipelineLogDestinationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetPipelineLogDestinationArrayOutput)
}

type GetPipelineLogDestinationOutput struct{ *pulumi.OutputState }

func (GetPipelineLogDestinationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPipelineLogDestination)(nil)).Elem()
}

func (o GetPipelineLogDestinationOutput) ToGetPipelineLogDestinationOutput() GetPipelineLogDestinationOutput {
	return o
}

func (o GetPipelineLogDestinationOutput) ToGetPipelineLogDestinationOutputWithContext(ctx context.Context) GetPipelineLogDestinationOutput {
	return o
}

// [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only.
func (o GetPipelineLogDestinationOutput) RetentionInDays() pulumi.IntOutput {
	return o.ApplyT(func(v GetPipelineLogDestination) int { return v.RetentionInDays }).(pulumi.IntOutput)
}

// [string] The internal output stream to send logs to.
func (o GetPipelineLogDestinationOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v GetPipelineLogDestination) string { return v.Type }).(pulumi.StringOutput)
}

type GetPipelineLogDestinationArrayOutput struct{ *pulumi.OutputState }

func (GetPipelineLogDestinationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetPipelineLogDestination)(nil)).Elem()
}

func (o GetPipelineLogDestinationArrayOutput) ToGetPipelineLogDestinationArrayOutput() GetPipelineLogDestinationArrayOutput {
	return o
}

func (o GetPipelineLogDestinationArrayOutput) ToGetPipelineLogDestinationArrayOutputWithContext(ctx context.Context) GetPipelineLogDestinationArrayOutput {
	return o
}

func (o GetPipelineLogDestinationArrayOutput) Index(i pulumi.IntInput) GetPipelineLogDestinationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetPipelineLogDestination {
		return vs[0].([]GetPipelineLogDestination)[vs[1].(int)]
	}).(GetPipelineLogDestinationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineLogInput)(nil)).Elem(), PipelineLogArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineLogArrayInput)(nil)).Elem(), PipelineLogArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineLogDestinationInput)(nil)).Elem(), PipelineLogDestinationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineLogDestinationArrayInput)(nil)).Elem(), PipelineLogDestinationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetPipelineLogInput)(nil)).Elem(), GetPipelineLogArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetPipelineLogArrayInput)(nil)).Elem(), GetPipelineLogArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetPipelineLogDestinationInput)(nil)).Elem(), GetPipelineLogDestinationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetPipelineLogDestinationArrayInput)(nil)).Elem(), GetPipelineLogDestinationArray{})
	pulumi.RegisterOutputType(PipelineLogOutput{})
	pulumi.RegisterOutputType(PipelineLogArrayOutput{})
	pulumi.RegisterOutputType(PipelineLogDestinationOutput{})
	pulumi.RegisterOutputType(PipelineLogDestinationArrayOutput{})
	pulumi.RegisterOutputType(GetPipelineLogOutput{})
	pulumi.RegisterOutputType(GetPipelineLogArrayOutput{})
	pulumi.RegisterOutputType(GetPipelineLogDestinationOutput{})
	pulumi.RegisterOutputType(GetPipelineLogDestinationArrayOutput{})
}

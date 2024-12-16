// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetImage(ctx *pulumi.Context, args *GetImageArgs, opts ...pulumi.InvokeOption) (*GetImageResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetImageResult
	err := ctx.Invoke("ionoscloud:index/getImage:getImage", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getImage.
type GetImageArgs struct {
	CloudInit   *string `pulumi:"cloudInit"`
	Description *string `pulumi:"description"`
	ImageAlias  *string `pulumi:"imageAlias"`
	Location    *string `pulumi:"location"`
	Name        *string `pulumi:"name"`
	Type        *string `pulumi:"type"`
	Version     *string `pulumi:"version"`
}

// A collection of values returned by getImage.
type GetImageResult struct {
	CloudInit           string  `pulumi:"cloudInit"`
	CpuHotPlug          bool    `pulumi:"cpuHotPlug"`
	CpuHotUnplug        bool    `pulumi:"cpuHotUnplug"`
	Description         *string `pulumi:"description"`
	DiscScsiHotPlug     bool    `pulumi:"discScsiHotPlug"`
	DiscScsiHotUnplug   bool    `pulumi:"discScsiHotUnplug"`
	DiscVirtioHotPlug   bool    `pulumi:"discVirtioHotPlug"`
	DiscVirtioHotUnplug bool    `pulumi:"discVirtioHotUnplug"`
	// The provider-assigned unique ID for this managed resource.
	Id           string   `pulumi:"id"`
	ImageAlias   *string  `pulumi:"imageAlias"`
	ImageAliases []string `pulumi:"imageAliases"`
	LicenceType  string   `pulumi:"licenceType"`
	Location     *string  `pulumi:"location"`
	Name         *string  `pulumi:"name"`
	NicHotPlug   bool     `pulumi:"nicHotPlug"`
	NicHotUnplug bool     `pulumi:"nicHotUnplug"`
	Public       bool     `pulumi:"public"`
	RamHotPlug   bool     `pulumi:"ramHotPlug"`
	RamHotUnplug bool     `pulumi:"ramHotUnplug"`
	Size         float64  `pulumi:"size"`
	Type         *string  `pulumi:"type"`
	Version      *string  `pulumi:"version"`
}

func GetImageOutput(ctx *pulumi.Context, args GetImageOutputArgs, opts ...pulumi.InvokeOption) GetImageResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetImageResultOutput, error) {
			args := v.(GetImageArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getImage:getImage", args, GetImageResultOutput{}, options).(GetImageResultOutput), nil
		}).(GetImageResultOutput)
}

// A collection of arguments for invoking getImage.
type GetImageOutputArgs struct {
	CloudInit   pulumi.StringPtrInput `pulumi:"cloudInit"`
	Description pulumi.StringPtrInput `pulumi:"description"`
	ImageAlias  pulumi.StringPtrInput `pulumi:"imageAlias"`
	Location    pulumi.StringPtrInput `pulumi:"location"`
	Name        pulumi.StringPtrInput `pulumi:"name"`
	Type        pulumi.StringPtrInput `pulumi:"type"`
	Version     pulumi.StringPtrInput `pulumi:"version"`
}

func (GetImageOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetImageArgs)(nil)).Elem()
}

// A collection of values returned by getImage.
type GetImageResultOutput struct{ *pulumi.OutputState }

func (GetImageResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetImageResult)(nil)).Elem()
}

func (o GetImageResultOutput) ToGetImageResultOutput() GetImageResultOutput {
	return o
}

func (o GetImageResultOutput) ToGetImageResultOutputWithContext(ctx context.Context) GetImageResultOutput {
	return o
}

func (o GetImageResultOutput) CloudInit() pulumi.StringOutput {
	return o.ApplyT(func(v GetImageResult) string { return v.CloudInit }).(pulumi.StringOutput)
}

func (o GetImageResultOutput) CpuHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.CpuHotPlug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) CpuHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.CpuHotUnplug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetImageResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o GetImageResultOutput) DiscScsiHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.DiscScsiHotPlug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) DiscScsiHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.DiscScsiHotUnplug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) DiscVirtioHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.DiscVirtioHotPlug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) DiscVirtioHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.DiscVirtioHotUnplug }).(pulumi.BoolOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetImageResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetImageResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetImageResultOutput) ImageAlias() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetImageResult) *string { return v.ImageAlias }).(pulumi.StringPtrOutput)
}

func (o GetImageResultOutput) ImageAliases() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetImageResult) []string { return v.ImageAliases }).(pulumi.StringArrayOutput)
}

func (o GetImageResultOutput) LicenceType() pulumi.StringOutput {
	return o.ApplyT(func(v GetImageResult) string { return v.LicenceType }).(pulumi.StringOutput)
}

func (o GetImageResultOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetImageResult) *string { return v.Location }).(pulumi.StringPtrOutput)
}

func (o GetImageResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetImageResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o GetImageResultOutput) NicHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.NicHotPlug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) NicHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.NicHotUnplug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) Public() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.Public }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) RamHotPlug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.RamHotPlug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) RamHotUnplug() pulumi.BoolOutput {
	return o.ApplyT(func(v GetImageResult) bool { return v.RamHotUnplug }).(pulumi.BoolOutput)
}

func (o GetImageResultOutput) Size() pulumi.Float64Output {
	return o.ApplyT(func(v GetImageResult) float64 { return v.Size }).(pulumi.Float64Output)
}

func (o GetImageResultOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetImageResult) *string { return v.Type }).(pulumi.StringPtrOutput)
}

func (o GetImageResultOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetImageResult) *string { return v.Version }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetImageResultOutput{})
}

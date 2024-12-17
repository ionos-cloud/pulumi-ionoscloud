// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Cube Server data source** can be used to search for and return existing servers.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
func GetCubeServer(ctx *pulumi.Context, args *GetCubeServerArgs, opts ...pulumi.InvokeOption) (*GetCubeServerResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetCubeServerResult
	err := ctx.Invoke("ionoscloud:index/getCubeServer:getCubeServer", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCubeServer.
type GetCubeServerArgs struct {
	// Datacenter's UUID.
	DatacenterId string `pulumi:"datacenterId"`
	// ID of the server you want to search for.
	//
	// `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// Name of an existing server that you want to search for.
	Name *string `pulumi:"name"`
	// The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
	TemplateUuid *string `pulumi:"templateUuid"`
}

// A collection of values returned by getCubeServer.
type GetCubeServerResult struct {
	// The availability zone in which the volume should exist
	AvailabilityZone string `pulumi:"availabilityZone"`
	BootCdrom        string `pulumi:"bootCdrom"`
	BootImage        string `pulumi:"bootImage"`
	BootVolume       string `pulumi:"bootVolume"`
	// list of
	Cdroms    []GetCubeServerCdrom `pulumi:"cdroms"`
	Cores     int                  `pulumi:"cores"`
	CpuFamily string               `pulumi:"cpuFamily"`
	// The id of the datacenter
	DatacenterId string `pulumi:"datacenterId"`
	// Id of the firewall rule
	Id *string `pulumi:"id"`
	// Name of the firewall rule
	Name *string `pulumi:"name"`
	// list of
	Nics []GetCubeServerNic `pulumi:"nics"`
	Ram  int                `pulumi:"ram"`
	// The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
	TemplateUuid *string `pulumi:"templateUuid"`
	Token        string  `pulumi:"token"`
	// Status of the virtual Machine
	VmState string `pulumi:"vmState"`
	// list of
	Volumes []GetCubeServerVolume `pulumi:"volumes"`
}

func GetCubeServerOutput(ctx *pulumi.Context, args GetCubeServerOutputArgs, opts ...pulumi.InvokeOption) GetCubeServerResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetCubeServerResultOutput, error) {
			args := v.(GetCubeServerArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getCubeServer:getCubeServer", args, GetCubeServerResultOutput{}, options).(GetCubeServerResultOutput), nil
		}).(GetCubeServerResultOutput)
}

// A collection of arguments for invoking getCubeServer.
type GetCubeServerOutputArgs struct {
	// Datacenter's UUID.
	DatacenterId pulumi.StringInput `pulumi:"datacenterId"`
	// ID of the server you want to search for.
	//
	// `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing server that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
	TemplateUuid pulumi.StringPtrInput `pulumi:"templateUuid"`
}

func (GetCubeServerOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCubeServerArgs)(nil)).Elem()
}

// A collection of values returned by getCubeServer.
type GetCubeServerResultOutput struct{ *pulumi.OutputState }

func (GetCubeServerResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCubeServerResult)(nil)).Elem()
}

func (o GetCubeServerResultOutput) ToGetCubeServerResultOutput() GetCubeServerResultOutput {
	return o
}

func (o GetCubeServerResultOutput) ToGetCubeServerResultOutputWithContext(ctx context.Context) GetCubeServerResultOutput {
	return o
}

// The availability zone in which the volume should exist
func (o GetCubeServerResultOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v GetCubeServerResult) string { return v.AvailabilityZone }).(pulumi.StringOutput)
}

func (o GetCubeServerResultOutput) BootCdrom() pulumi.StringOutput {
	return o.ApplyT(func(v GetCubeServerResult) string { return v.BootCdrom }).(pulumi.StringOutput)
}

func (o GetCubeServerResultOutput) BootImage() pulumi.StringOutput {
	return o.ApplyT(func(v GetCubeServerResult) string { return v.BootImage }).(pulumi.StringOutput)
}

func (o GetCubeServerResultOutput) BootVolume() pulumi.StringOutput {
	return o.ApplyT(func(v GetCubeServerResult) string { return v.BootVolume }).(pulumi.StringOutput)
}

// list of
func (o GetCubeServerResultOutput) Cdroms() GetCubeServerCdromArrayOutput {
	return o.ApplyT(func(v GetCubeServerResult) []GetCubeServerCdrom { return v.Cdroms }).(GetCubeServerCdromArrayOutput)
}

func (o GetCubeServerResultOutput) Cores() pulumi.IntOutput {
	return o.ApplyT(func(v GetCubeServerResult) int { return v.Cores }).(pulumi.IntOutput)
}

func (o GetCubeServerResultOutput) CpuFamily() pulumi.StringOutput {
	return o.ApplyT(func(v GetCubeServerResult) string { return v.CpuFamily }).(pulumi.StringOutput)
}

// The id of the datacenter
func (o GetCubeServerResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetCubeServerResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// Id of the firewall rule
func (o GetCubeServerResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCubeServerResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Name of the firewall rule
func (o GetCubeServerResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCubeServerResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// list of
func (o GetCubeServerResultOutput) Nics() GetCubeServerNicArrayOutput {
	return o.ApplyT(func(v GetCubeServerResult) []GetCubeServerNic { return v.Nics }).(GetCubeServerNicArrayOutput)
}

func (o GetCubeServerResultOutput) Ram() pulumi.IntOutput {
	return o.ApplyT(func(v GetCubeServerResult) int { return v.Ram }).(pulumi.IntOutput)
}

// The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
func (o GetCubeServerResultOutput) TemplateUuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCubeServerResult) *string { return v.TemplateUuid }).(pulumi.StringPtrOutput)
}

func (o GetCubeServerResultOutput) Token() pulumi.StringOutput {
	return o.ApplyT(func(v GetCubeServerResult) string { return v.Token }).(pulumi.StringOutput)
}

// Status of the virtual Machine
func (o GetCubeServerResultOutput) VmState() pulumi.StringOutput {
	return o.ApplyT(func(v GetCubeServerResult) string { return v.VmState }).(pulumi.StringOutput)
}

// list of
func (o GetCubeServerResultOutput) Volumes() GetCubeServerVolumeArrayOutput {
	return o.ApplyT(func(v GetCubeServerResult) []GetCubeServerVolume { return v.Volumes }).(GetCubeServerVolumeArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetCubeServerResultOutput{})
}

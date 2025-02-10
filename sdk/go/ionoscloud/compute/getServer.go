// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Server data source** can be used to search for and return existing servers.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By ID
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
//			_, err := compute.LookupServer(ctx, &compute.LookupServerArgs{
//				DatacenterId: "datacenter_id",
//				Id:           pulumi.StringRef("server_id"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ### By Name
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
//			_, err := compute.LookupServer(ctx, &compute.LookupServerArgs{
//				DatacenterId: "datacenter_id",
//				Name:         pulumi.StringRef("Server Example"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupServer(ctx *pulumi.Context, args *LookupServerArgs, opts ...pulumi.InvokeOption) (*LookupServerResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupServerResult
	err := ctx.Invoke("ionoscloud:compute/getServer:getServer", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getServer.
type LookupServerArgs struct {
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
	// The type of firewall rule
	Type *string `pulumi:"type"`
}

// A collection of values returned by getServer.
type LookupServerResult struct {
	// The availability zone in which the volume should exist
	AvailabilityZone string `pulumi:"availabilityZone"`
	BootCdrom        string `pulumi:"bootCdrom"`
	BootImage        string `pulumi:"bootImage"`
	BootVolume       string `pulumi:"bootVolume"`
	// list of
	Cdroms []GetServerCdrom `pulumi:"cdroms"`
	// The total number of cores for the server
	Cores int `pulumi:"cores"`
	// CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource.
	CpuFamily string `pulumi:"cpuFamily"`
	// The id of the datacenter
	DatacenterId string `pulumi:"datacenterId"`
	// The hostname of the resource.
	Hostname string `pulumi:"hostname"`
	// The Id of the label
	Id string `pulumi:"id"`
	// list of
	Labels []GetServerLabel `pulumi:"labels"`
	// Name of the firewall rule
	Name string `pulumi:"name"`
	// list of
	Nics []GetServerNic `pulumi:"nics"`
	// The amount of memory for the server in MB
	Ram int `pulumi:"ram"`
	// The list of Security Group IDs for the resource.
	SecurityGroupsIds []string `pulumi:"securityGroupsIds"`
	// The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
	TemplateUuid *string `pulumi:"templateUuid"`
	Token        string  `pulumi:"token"`
	// The type of firewall rule
	Type string `pulumi:"type"`
	// Status of the virtual Machine
	VmState string `pulumi:"vmState"`
	// list of
	Volumes []GetServerVolume `pulumi:"volumes"`
}

func LookupServerOutput(ctx *pulumi.Context, args LookupServerOutputArgs, opts ...pulumi.InvokeOption) LookupServerResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupServerResultOutput, error) {
			args := v.(LookupServerArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:compute/getServer:getServer", args, LookupServerResultOutput{}, options).(LookupServerResultOutput), nil
		}).(LookupServerResultOutput)
}

// A collection of arguments for invoking getServer.
type LookupServerOutputArgs struct {
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
	// The type of firewall rule
	Type pulumi.StringPtrInput `pulumi:"type"`
}

func (LookupServerOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupServerArgs)(nil)).Elem()
}

// A collection of values returned by getServer.
type LookupServerResultOutput struct{ *pulumi.OutputState }

func (LookupServerResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupServerResult)(nil)).Elem()
}

func (o LookupServerResultOutput) ToLookupServerResultOutput() LookupServerResultOutput {
	return o
}

func (o LookupServerResultOutput) ToLookupServerResultOutputWithContext(ctx context.Context) LookupServerResultOutput {
	return o
}

// The availability zone in which the volume should exist
func (o LookupServerResultOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.AvailabilityZone }).(pulumi.StringOutput)
}

func (o LookupServerResultOutput) BootCdrom() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.BootCdrom }).(pulumi.StringOutput)
}

func (o LookupServerResultOutput) BootImage() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.BootImage }).(pulumi.StringOutput)
}

func (o LookupServerResultOutput) BootVolume() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.BootVolume }).(pulumi.StringOutput)
}

// list of
func (o LookupServerResultOutput) Cdroms() GetServerCdromArrayOutput {
	return o.ApplyT(func(v LookupServerResult) []GetServerCdrom { return v.Cdroms }).(GetServerCdromArrayOutput)
}

// The total number of cores for the server
func (o LookupServerResultOutput) Cores() pulumi.IntOutput {
	return o.ApplyT(func(v LookupServerResult) int { return v.Cores }).(pulumi.IntOutput)
}

// CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource.
func (o LookupServerResultOutput) CpuFamily() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.CpuFamily }).(pulumi.StringOutput)
}

// The id of the datacenter
func (o LookupServerResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// The hostname of the resource.
func (o LookupServerResultOutput) Hostname() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.Hostname }).(pulumi.StringOutput)
}

// The Id of the label
func (o LookupServerResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.Id }).(pulumi.StringOutput)
}

// list of
func (o LookupServerResultOutput) Labels() GetServerLabelArrayOutput {
	return o.ApplyT(func(v LookupServerResult) []GetServerLabel { return v.Labels }).(GetServerLabelArrayOutput)
}

// Name of the firewall rule
func (o LookupServerResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.Name }).(pulumi.StringOutput)
}

// list of
func (o LookupServerResultOutput) Nics() GetServerNicArrayOutput {
	return o.ApplyT(func(v LookupServerResult) []GetServerNic { return v.Nics }).(GetServerNicArrayOutput)
}

// The amount of memory for the server in MB
func (o LookupServerResultOutput) Ram() pulumi.IntOutput {
	return o.ApplyT(func(v LookupServerResult) int { return v.Ram }).(pulumi.IntOutput)
}

// The list of Security Group IDs for the resource.
func (o LookupServerResultOutput) SecurityGroupsIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupServerResult) []string { return v.SecurityGroupsIds }).(pulumi.StringArrayOutput)
}

// The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
func (o LookupServerResultOutput) TemplateUuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupServerResult) *string { return v.TemplateUuid }).(pulumi.StringPtrOutput)
}

func (o LookupServerResultOutput) Token() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.Token }).(pulumi.StringOutput)
}

// The type of firewall rule
func (o LookupServerResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.Type }).(pulumi.StringOutput)
}

// Status of the virtual Machine
func (o LookupServerResultOutput) VmState() pulumi.StringOutput {
	return o.ApplyT(func(v LookupServerResult) string { return v.VmState }).(pulumi.StringOutput)
}

// list of
func (o LookupServerResultOutput) Volumes() GetServerVolumeArrayOutput {
	return o.ApplyT(func(v LookupServerResult) []GetServerVolume { return v.Volumes }).(GetServerVolumeArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupServerResultOutput{})
}

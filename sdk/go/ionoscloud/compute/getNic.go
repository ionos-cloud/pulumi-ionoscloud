// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Nic data source** can be used to search for and return existing nics.
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
//			_, err := compute.LookupNic(ctx, &compute.LookupNicArgs{
//				DatacenterId: "datancenter_id",
//				ServerId:     "server_id",
//				Id:           pulumi.StringRef("nic_id"),
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
//			_, err := compute.LookupNic(ctx, &compute.LookupNicArgs{
//				DatacenterId: "datancenter_id",
//				ServerId:     "server_id",
//				Name:         pulumi.StringRef("Nic Example"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupNic(ctx *pulumi.Context, args *LookupNicArgs, opts ...pulumi.InvokeOption) (*LookupNicResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNicResult
	err := ctx.Invoke("ionoscloud:compute/getNic:getNic", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNic.
type LookupNicArgs struct {
	// [string] The ID of a Virtual Data Center.
	DatacenterId string `pulumi:"datacenterId"`
	// ID of the nic you want to search for.
	//
	// `datacenterId` and either `name` or `id` must be provided.
	// If none, are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// [string] The name of the LAN.
	Name *string `pulumi:"name"`
	// [string] The ID of a server.
	ServerId string `pulumi:"serverId"`
}

// A collection of values returned by getNic.
type LookupNicResult struct {
	// The ID of a Virtual Data Center.
	DatacenterId string `pulumi:"datacenterId"`
	// The Logical Unit Number (LUN) of the storage volume. Null if this NIC was created from CloudAPI and no DCD changes were done on the Datacenter.
	DeviceNumber int `pulumi:"deviceNumber"`
	// Indicates if the NIC should get an IP address using DHCP (true) or not (false).
	Dhcp   bool `pulumi:"dhcp"`
	Dhcpv6 bool `pulumi:"dhcpv6"`
	// If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
	FirewallActive bool `pulumi:"firewallActive"`
	// The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
	FirewallType string `pulumi:"firewallType"`
	// Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
	Flowlogs []GetNicFlowlog `pulumi:"flowlogs"`
	// The id of the NIC.
	Id string `pulumi:"id"`
	// Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
	Ips           []string `pulumi:"ips"`
	Ipv6CidrBlock string   `pulumi:"ipv6CidrBlock"`
	Ipv6Ips       []string `pulumi:"ipv6Ips"`
	// The LAN ID the NIC will sit on.
	Lan int `pulumi:"lan"`
	// The MAC address of the NIC.
	Mac string `pulumi:"mac"`
	// Specifies the name of the flow log.
	Name string `pulumi:"name"`
	// The PCI slot number of the Nic.
	PciSlot int `pulumi:"pciSlot"`
	// The list of Security Group IDs for the resource.
	SecurityGroupsIds []string `pulumi:"securityGroupsIds"`
	// The ID of a server.
	ServerId string `pulumi:"serverId"`
}

func LookupNicOutput(ctx *pulumi.Context, args LookupNicOutputArgs, opts ...pulumi.InvokeOption) LookupNicResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupNicResultOutput, error) {
			args := v.(LookupNicArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:compute/getNic:getNic", args, LookupNicResultOutput{}, options).(LookupNicResultOutput), nil
		}).(LookupNicResultOutput)
}

// A collection of arguments for invoking getNic.
type LookupNicOutputArgs struct {
	// [string] The ID of a Virtual Data Center.
	DatacenterId pulumi.StringInput `pulumi:"datacenterId"`
	// ID of the nic you want to search for.
	//
	// `datacenterId` and either `name` or `id` must be provided.
	// If none, are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// [string] The name of the LAN.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// [string] The ID of a server.
	ServerId pulumi.StringInput `pulumi:"serverId"`
}

func (LookupNicOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNicArgs)(nil)).Elem()
}

// A collection of values returned by getNic.
type LookupNicResultOutput struct{ *pulumi.OutputState }

func (LookupNicResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNicResult)(nil)).Elem()
}

func (o LookupNicResultOutput) ToLookupNicResultOutput() LookupNicResultOutput {
	return o
}

func (o LookupNicResultOutput) ToLookupNicResultOutputWithContext(ctx context.Context) LookupNicResultOutput {
	return o
}

// The ID of a Virtual Data Center.
func (o LookupNicResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNicResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// The Logical Unit Number (LUN) of the storage volume. Null if this NIC was created from CloudAPI and no DCD changes were done on the Datacenter.
func (o LookupNicResultOutput) DeviceNumber() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNicResult) int { return v.DeviceNumber }).(pulumi.IntOutput)
}

// Indicates if the NIC should get an IP address using DHCP (true) or not (false).
func (o LookupNicResultOutput) Dhcp() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupNicResult) bool { return v.Dhcp }).(pulumi.BoolOutput)
}

func (o LookupNicResultOutput) Dhcpv6() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupNicResult) bool { return v.Dhcpv6 }).(pulumi.BoolOutput)
}

// If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
func (o LookupNicResultOutput) FirewallActive() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupNicResult) bool { return v.FirewallActive }).(pulumi.BoolOutput)
}

// The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
func (o LookupNicResultOutput) FirewallType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNicResult) string { return v.FirewallType }).(pulumi.StringOutput)
}

// Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
func (o LookupNicResultOutput) Flowlogs() GetNicFlowlogArrayOutput {
	return o.ApplyT(func(v LookupNicResult) []GetNicFlowlog { return v.Flowlogs }).(GetNicFlowlogArrayOutput)
}

// The id of the NIC.
func (o LookupNicResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNicResult) string { return v.Id }).(pulumi.StringOutput)
}

// Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
func (o LookupNicResultOutput) Ips() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNicResult) []string { return v.Ips }).(pulumi.StringArrayOutput)
}

func (o LookupNicResultOutput) Ipv6CidrBlock() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNicResult) string { return v.Ipv6CidrBlock }).(pulumi.StringOutput)
}

func (o LookupNicResultOutput) Ipv6Ips() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNicResult) []string { return v.Ipv6Ips }).(pulumi.StringArrayOutput)
}

// The LAN ID the NIC will sit on.
func (o LookupNicResultOutput) Lan() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNicResult) int { return v.Lan }).(pulumi.IntOutput)
}

// The MAC address of the NIC.
func (o LookupNicResultOutput) Mac() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNicResult) string { return v.Mac }).(pulumi.StringOutput)
}

// Specifies the name of the flow log.
func (o LookupNicResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNicResult) string { return v.Name }).(pulumi.StringOutput)
}

// The PCI slot number of the Nic.
func (o LookupNicResultOutput) PciSlot() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNicResult) int { return v.PciSlot }).(pulumi.IntOutput)
}

// The list of Security Group IDs for the resource.
func (o LookupNicResultOutput) SecurityGroupsIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNicResult) []string { return v.SecurityGroupsIds }).(pulumi.StringArrayOutput)
}

// The ID of a server.
func (o LookupNicResultOutput) ServerId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNicResult) string { return v.ServerId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNicResultOutput{})
}

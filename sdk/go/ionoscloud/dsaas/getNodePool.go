// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dsaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Dataplatform Node Pool Data Source** can be used to search for and return an existing Dataplatform Node Pool under a Dataplatform Cluster.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search and make sure that your resources have unique names.
//
// ## Example Usage
//
// ### By ID
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dsaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dsaas.LookupNodePool(ctx, &dsaas.LookupNodePoolArgs{
//				ClusterId: "cluster_id",
//				Id:        pulumi.StringRef("node_pool_id"),
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
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dsaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dsaas.LookupNodePool(ctx, &dsaas.LookupNodePoolArgs{
//				ClusterId: "cluster_id",
//				Name:      pulumi.StringRef("Dataplatform_Node_Pool_Example"),
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
// ### By Name with Partial Match
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dsaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dsaas.LookupNodePool(ctx, &dsaas.LookupNodePoolArgs{
//				ClusterId:    "cluster_id",
//				Name:         pulumi.StringRef("_Example"),
//				PartialMatch: pulumi.BoolRef(true),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupNodePool(ctx *pulumi.Context, args *LookupNodePoolArgs, opts ...pulumi.InvokeOption) (*LookupNodePoolResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNodePoolResult
	err := ctx.Invoke("ionoscloud:dsaas/getNodePool:getNodePool", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNodePool.
type LookupNodePoolArgs struct {
	// ID of the cluster the searched node pool is part of.
	ClusterId string `pulumi:"clusterId"`
	// ID of the node pool you want to search for.
	Id *string `pulumi:"id"`
	// Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
	Name *string `pulumi:"name"`
	// Whether partial matching is allowed or not when using name argument. Default value is false.
	//
	// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
	PartialMatch *bool `pulumi:"partialMatch"`
}

// A collection of values returned by getNodePool.
type LookupNodePoolResult struct {
	// Key-value pairs attached to node pool resource as [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).
	Annotations map[string]string `pulumi:"annotations"`
	// Whether the Node Pool should autoscale. For more details, please check the API documentation
	AutoScalings []GetNodePoolAutoScaling `pulumi:"autoScalings"`
	// The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
	AvailabilityZone string `pulumi:"availabilityZone"`
	// ID of the cluster the searched node pool is part of.
	ClusterId string `pulumi:"clusterId"`
	// The number of CPU cores per node.
	CoresCount int `pulumi:"coresCount"`
	// A CPU family.
	CpuFamily string `pulumi:"cpuFamily"`
	// The UUID of the virtual data center (VDC) the cluster is provisioned.
	DatacenterId string `pulumi:"datacenterId"`
	// ID of your node pool.
	Id string `pulumi:"id"`
	// Key-value pairs attached to the node pool resource as [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
	Labels map[string]string `pulumi:"labels"`
	// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
	MaintenanceWindows []GetNodePoolMaintenanceWindow `pulumi:"maintenanceWindows"`
	// The name of your node pool
	Name string `pulumi:"name"`
	// The number of nodes that make up the node pool.
	NodeCount    int   `pulumi:"nodeCount"`
	PartialMatch *bool `pulumi:"partialMatch"`
	// The RAM size for one node in MB.
	RamSize int `pulumi:"ramSize"`
	// The size of the volume in GB.
	StorageSize int `pulumi:"storageSize"`
	// The type of hardware for the volume.
	StorageType string `pulumi:"storageType"`
	// The version of the Data Platform.
	Version string `pulumi:"version"`
}

func LookupNodePoolOutput(ctx *pulumi.Context, args LookupNodePoolOutputArgs, opts ...pulumi.InvokeOption) LookupNodePoolResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupNodePoolResultOutput, error) {
			args := v.(LookupNodePoolArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:dsaas/getNodePool:getNodePool", args, LookupNodePoolResultOutput{}, options).(LookupNodePoolResultOutput), nil
		}).(LookupNodePoolResultOutput)
}

// A collection of arguments for invoking getNodePool.
type LookupNodePoolOutputArgs struct {
	// ID of the cluster the searched node pool is part of.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// ID of the node pool you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Whether partial matching is allowed or not when using name argument. Default value is false.
	//
	// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
	PartialMatch pulumi.BoolPtrInput `pulumi:"partialMatch"`
}

func (LookupNodePoolOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNodePoolArgs)(nil)).Elem()
}

// A collection of values returned by getNodePool.
type LookupNodePoolResultOutput struct{ *pulumi.OutputState }

func (LookupNodePoolResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNodePoolResult)(nil)).Elem()
}

func (o LookupNodePoolResultOutput) ToLookupNodePoolResultOutput() LookupNodePoolResultOutput {
	return o
}

func (o LookupNodePoolResultOutput) ToLookupNodePoolResultOutputWithContext(ctx context.Context) LookupNodePoolResultOutput {
	return o
}

// Key-value pairs attached to node pool resource as [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).
func (o LookupNodePoolResultOutput) Annotations() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupNodePoolResult) map[string]string { return v.Annotations }).(pulumi.StringMapOutput)
}

// Whether the Node Pool should autoscale. For more details, please check the API documentation
func (o LookupNodePoolResultOutput) AutoScalings() GetNodePoolAutoScalingArrayOutput {
	return o.ApplyT(func(v LookupNodePoolResult) []GetNodePoolAutoScaling { return v.AutoScalings }).(GetNodePoolAutoScalingArrayOutput)
}

// The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
func (o LookupNodePoolResultOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.AvailabilityZone }).(pulumi.StringOutput)
}

// ID of the cluster the searched node pool is part of.
func (o LookupNodePoolResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// The number of CPU cores per node.
func (o LookupNodePoolResultOutput) CoresCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNodePoolResult) int { return v.CoresCount }).(pulumi.IntOutput)
}

// A CPU family.
func (o LookupNodePoolResultOutput) CpuFamily() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.CpuFamily }).(pulumi.StringOutput)
}

// The UUID of the virtual data center (VDC) the cluster is provisioned.
func (o LookupNodePoolResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// ID of your node pool.
func (o LookupNodePoolResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.Id }).(pulumi.StringOutput)
}

// Key-value pairs attached to the node pool resource as [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
func (o LookupNodePoolResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupNodePoolResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
func (o LookupNodePoolResultOutput) MaintenanceWindows() GetNodePoolMaintenanceWindowArrayOutput {
	return o.ApplyT(func(v LookupNodePoolResult) []GetNodePoolMaintenanceWindow { return v.MaintenanceWindows }).(GetNodePoolMaintenanceWindowArrayOutput)
}

// The name of your node pool
func (o LookupNodePoolResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.Name }).(pulumi.StringOutput)
}

// The number of nodes that make up the node pool.
func (o LookupNodePoolResultOutput) NodeCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNodePoolResult) int { return v.NodeCount }).(pulumi.IntOutput)
}

func (o LookupNodePoolResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupNodePoolResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// The RAM size for one node in MB.
func (o LookupNodePoolResultOutput) RamSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNodePoolResult) int { return v.RamSize }).(pulumi.IntOutput)
}

// The size of the volume in GB.
func (o LookupNodePoolResultOutput) StorageSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNodePoolResult) int { return v.StorageSize }).(pulumi.IntOutput)
}

// The type of hardware for the volume.
func (o LookupNodePoolResultOutput) StorageType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.StorageType }).(pulumi.StringOutput)
}

// The version of the Data Platform.
func (o LookupNodePoolResultOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNodePoolResult) string { return v.Version }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNodePoolResultOutput{})
}

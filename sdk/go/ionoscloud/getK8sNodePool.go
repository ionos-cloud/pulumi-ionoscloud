// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **k8s Node Pool** data source can be used to search for and return existing k8s Node Pools.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
func GetK8sNodePool(ctx *pulumi.Context, args *GetK8sNodePoolArgs, opts ...pulumi.InvokeOption) (*GetK8sNodePoolResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetK8sNodePoolResult
	err := ctx.Invoke("ionoscloud:index/getK8sNodePool:getK8sNodePool", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getK8sNodePool.
type GetK8sNodePoolArgs struct {
	// ID of the node pool you want to search for.
	//
	// `k8sClusterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// K8s Cluster' UUID
	K8sClusterId string `pulumi:"k8sClusterId"`
	// Name of an existing node pool that you want to search for.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getK8sNodePool.
type GetK8sNodePoolResult struct {
	// A map of annotations in the form of key > value
	Annotations map[string]string `pulumi:"annotations"`
	// The range defining the minimum and maximum number of worker nodes that the managed node group can scale in
	AutoScalings []GetK8sNodePoolAutoScaling `pulumi:"autoScalings"`
	// The compute availability zone in which the nodes should exist
	AvailabilityZone string `pulumi:"availabilityZone"`
	// A list of kubernetes versions available for upgrade
	AvailableUpgradeVersions []string `pulumi:"availableUpgradeVersions"`
	// CPU cores count
	CoresCount int `pulumi:"coresCount"`
	// CPU Family
	CpuFamily string `pulumi:"cpuFamily"`
	// The UUID of the VDC
	DatacenterId string `pulumi:"datacenterId"`
	// The LAN ID of an existing LAN at the related datacenter
	Id *string `pulumi:"id"`
	// ID of the cluster this node pool is part of
	K8sClusterId string `pulumi:"k8sClusterId"`
	// The kubernetes version
	K8sVersion string `pulumi:"k8sVersion"`
	// A map of labels in the form of key > value
	Labels map[string]string `pulumi:"labels"`
	// A list of Local Area Networks the node pool is a part of
	Lans []GetK8sNodePoolLan `pulumi:"lans"`
	// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
	MaintenanceWindows []GetK8sNodePoolMaintenanceWindow `pulumi:"maintenanceWindows"`
	// name of the node pool
	Name *string `pulumi:"name"`
	// The number of nodes in this node pool
	NodeCount int `pulumi:"nodeCount"`
	// The list of fixed IPs associated with this node pool
	PublicIps []string `pulumi:"publicIps"`
	// The amount of RAM in MB
	RamSize int `pulumi:"ramSize"`
	// one of "AVAILABLE",
	// "INACTIVE",
	// "BUSY",
	// "DEPLOYING",
	// "ACTIVE",
	// "FAILED",
	// "SUSPENDED",
	// "FAILED_SUSPENDED",
	// "UPDATING",
	// "FAILED_UPDATING",
	// "DESTROYING",
	// "FAILED_DESTROYING",
	// "TERMINATED"
	State string `pulumi:"state"`
	// The size of the volume in GB. The size should be greater than 10GB.
	StorageSize int `pulumi:"storageSize"`
	// HDD or SDD
	StorageType string `pulumi:"storageType"`
}

func GetK8sNodePoolOutput(ctx *pulumi.Context, args GetK8sNodePoolOutputArgs, opts ...pulumi.InvokeOption) GetK8sNodePoolResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetK8sNodePoolResultOutput, error) {
			args := v.(GetK8sNodePoolArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getK8sNodePool:getK8sNodePool", args, GetK8sNodePoolResultOutput{}, options).(GetK8sNodePoolResultOutput), nil
		}).(GetK8sNodePoolResultOutput)
}

// A collection of arguments for invoking getK8sNodePool.
type GetK8sNodePoolOutputArgs struct {
	// ID of the node pool you want to search for.
	//
	// `k8sClusterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// K8s Cluster' UUID
	K8sClusterId pulumi.StringInput `pulumi:"k8sClusterId"`
	// Name of an existing node pool that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (GetK8sNodePoolOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetK8sNodePoolArgs)(nil)).Elem()
}

// A collection of values returned by getK8sNodePool.
type GetK8sNodePoolResultOutput struct{ *pulumi.OutputState }

func (GetK8sNodePoolResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetK8sNodePoolResult)(nil)).Elem()
}

func (o GetK8sNodePoolResultOutput) ToGetK8sNodePoolResultOutput() GetK8sNodePoolResultOutput {
	return o
}

func (o GetK8sNodePoolResultOutput) ToGetK8sNodePoolResultOutputWithContext(ctx context.Context) GetK8sNodePoolResultOutput {
	return o
}

// A map of annotations in the form of key > value
func (o GetK8sNodePoolResultOutput) Annotations() pulumi.StringMapOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) map[string]string { return v.Annotations }).(pulumi.StringMapOutput)
}

// The range defining the minimum and maximum number of worker nodes that the managed node group can scale in
func (o GetK8sNodePoolResultOutput) AutoScalings() GetK8sNodePoolAutoScalingArrayOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) []GetK8sNodePoolAutoScaling { return v.AutoScalings }).(GetK8sNodePoolAutoScalingArrayOutput)
}

// The compute availability zone in which the nodes should exist
func (o GetK8sNodePoolResultOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) string { return v.AvailabilityZone }).(pulumi.StringOutput)
}

// A list of kubernetes versions available for upgrade
func (o GetK8sNodePoolResultOutput) AvailableUpgradeVersions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) []string { return v.AvailableUpgradeVersions }).(pulumi.StringArrayOutput)
}

// CPU cores count
func (o GetK8sNodePoolResultOutput) CoresCount() pulumi.IntOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) int { return v.CoresCount }).(pulumi.IntOutput)
}

// CPU Family
func (o GetK8sNodePoolResultOutput) CpuFamily() pulumi.StringOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) string { return v.CpuFamily }).(pulumi.StringOutput)
}

// The UUID of the VDC
func (o GetK8sNodePoolResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// The LAN ID of an existing LAN at the related datacenter
func (o GetK8sNodePoolResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// ID of the cluster this node pool is part of
func (o GetK8sNodePoolResultOutput) K8sClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) string { return v.K8sClusterId }).(pulumi.StringOutput)
}

// The kubernetes version
func (o GetK8sNodePoolResultOutput) K8sVersion() pulumi.StringOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) string { return v.K8sVersion }).(pulumi.StringOutput)
}

// A map of labels in the form of key > value
func (o GetK8sNodePoolResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// A list of Local Area Networks the node pool is a part of
func (o GetK8sNodePoolResultOutput) Lans() GetK8sNodePoolLanArrayOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) []GetK8sNodePoolLan { return v.Lans }).(GetK8sNodePoolLanArrayOutput)
}

// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
func (o GetK8sNodePoolResultOutput) MaintenanceWindows() GetK8sNodePoolMaintenanceWindowArrayOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) []GetK8sNodePoolMaintenanceWindow { return v.MaintenanceWindows }).(GetK8sNodePoolMaintenanceWindowArrayOutput)
}

// name of the node pool
func (o GetK8sNodePoolResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The number of nodes in this node pool
func (o GetK8sNodePoolResultOutput) NodeCount() pulumi.IntOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) int { return v.NodeCount }).(pulumi.IntOutput)
}

// The list of fixed IPs associated with this node pool
func (o GetK8sNodePoolResultOutput) PublicIps() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) []string { return v.PublicIps }).(pulumi.StringArrayOutput)
}

// The amount of RAM in MB
func (o GetK8sNodePoolResultOutput) RamSize() pulumi.IntOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) int { return v.RamSize }).(pulumi.IntOutput)
}

// one of "AVAILABLE",
// "INACTIVE",
// "BUSY",
// "DEPLOYING",
// "ACTIVE",
// "FAILED",
// "SUSPENDED",
// "FAILED_SUSPENDED",
// "UPDATING",
// "FAILED_UPDATING",
// "DESTROYING",
// "FAILED_DESTROYING",
// "TERMINATED"
func (o GetK8sNodePoolResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) string { return v.State }).(pulumi.StringOutput)
}

// The size of the volume in GB. The size should be greater than 10GB.
func (o GetK8sNodePoolResultOutput) StorageSize() pulumi.IntOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) int { return v.StorageSize }).(pulumi.IntOutput)
}

// HDD or SDD
func (o GetK8sNodePoolResultOutput) StorageType() pulumi.StringOutput {
	return o.ApplyT(func(v GetK8sNodePoolResult) string { return v.StorageType }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetK8sNodePoolResultOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **Managed Kubernetes Cluster** on IonosCloud.
//
// ## Example Usage
//
// ### Public cluster
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := ionoscloud.NewK8sCluster(ctx, "example", &ionoscloud.K8sClusterArgs{
//				ApiSubnetAllowLists: pulumi.StringArray{
//					pulumi.String("1.2.3.4/32"),
//				},
//				K8sVersion: pulumi.String("1.28.6"),
//				MaintenanceWindow: &ionoscloud.K8sClusterMaintenanceWindowArgs{
//					DayOfTheWeek: pulumi.String("Sunday"),
//					Time:         pulumi.String("09:00:00Z"),
//				},
//				S3Buckets: ionoscloud.K8sClusterS3BucketArray{
//					&ionoscloud.K8sClusterS3BucketArgs{
//						Name: pulumi.String("globally_unique_bucket_name"),
//					},
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
// <!--End PulumiCodeChooser -->
//
// ### Private Cluster
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := compute.NewDatacenter(ctx, "testdatacenter", &compute.DatacenterArgs{
//				Location:    pulumi.String("de/fra"),
//				Description: pulumi.String("Test datacenter"),
//			})
//			if err != nil {
//				return err
//			}
//			k8sip, err := compute.NewIPBlock(ctx, "k8sip", &compute.IPBlockArgs{
//				Location: pulumi.String("de/fra"),
//				Size:     pulumi.Int(1),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ionoscloud.NewK8sCluster(ctx, "example", &ionoscloud.K8sClusterArgs{
//				K8sVersion: pulumi.String("1.28.6"),
//				MaintenanceWindow: &ionoscloud.K8sClusterMaintenanceWindowArgs{
//					DayOfTheWeek: pulumi.String("Sunday"),
//					Time:         pulumi.String("09:00:00Z"),
//				},
//				ApiSubnetAllowLists: pulumi.StringArray{
//					pulumi.String("1.2.3.4/32"),
//				},
//				S3Buckets: ionoscloud.K8sClusterS3BucketArray{
//					&ionoscloud.K8sClusterS3BucketArgs{
//						Name: pulumi.String("globally_unique_bucket_name"),
//					},
//				},
//				Location: pulumi.String("de/fra"),
//				NatGatewayIp: k8sip.Ips.ApplyT(func(ips []string) (string, error) {
//					return ips[0], nil
//				}).(pulumi.StringOutput),
//				NodeSubnet: pulumi.String("192.168.0.0/16"),
//				Public:     pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// A Kubernetes Cluster resource can be imported using its `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:index/k8sCluster:K8sCluster demo {k8s_cluster uuid}
// ```
//
// This can be helpful when you want to import kubernetes clusters which you have already created manually or using other means, outside of terraform.
//
// ⚠️ **_Warning: **During a maintenance window, k8s can update your `k8s_version` if the old one reaches end of life. This upgrade will not be shown in the plan, as we prevent
//
// terraform from doing a downgrade, as downgrading `k8s_version` is not supported._**
type K8sCluster struct {
	pulumi.CustomResourceState

	// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the cluster.
	//
	// ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the cluster in order to do it. Set the field to true only if you know what you are doing._**
	AllowReplace pulumi.BoolPtrOutput `pulumi:"allowReplace"`
	// [list] Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.
	ApiSubnetAllowLists pulumi.StringArrayOutput `pulumi:"apiSubnetAllowLists"`
	// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
	K8sVersion pulumi.StringOutput `pulumi:"k8sVersion"`
	// [string] This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have a data center at that location. This property is not adjustable.
	Location pulumi.StringPtrOutput `pulumi:"location"`
	// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
	MaintenanceWindow K8sClusterMaintenanceWindowOutput `pulumi:"maintenanceWindow"`
	// [string] The name of the Kubernetes Cluster.
	Name pulumi.StringOutput `pulumi:"name"`
	// [string] The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the same location as the cluster's location. This attribute is mandatory if the cluster is private.
	NatGatewayIp pulumi.StringPtrOutput `pulumi:"natGatewayIp"`
	// [string] The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid CIDR notation for an IPv4 network prefix of 16 bits length.
	NodeSubnet pulumi.StringOutput `pulumi:"nodeSubnet"`
	// [boolean] Indicates if the cluster is public or private. This attribute is immutable.
	Public pulumi.BoolPtrOutput `pulumi:"public"`
	// [list] List of IONOS Object Storage buckets configured for K8s usage. For now it contains only an IONOS Object Storage bucket used to store K8s API audit logs.
	S3Buckets K8sClusterS3BucketArrayOutput `pulumi:"s3Buckets"`
	// [list] List of versions that may be used for node pools under this cluster
	ViableNodePoolVersions pulumi.StringArrayOutput `pulumi:"viableNodePoolVersions"`
}

// NewK8sCluster registers a new resource with the given unique name, arguments, and options.
func NewK8sCluster(ctx *pulumi.Context,
	name string, args *K8sClusterArgs, opts ...pulumi.ResourceOption) (*K8sCluster, error) {
	if args == nil {
		args = &K8sClusterArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource K8sCluster
	err := ctx.RegisterResource("ionoscloud:index/k8sCluster:K8sCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetK8sCluster gets an existing K8sCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetK8sCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *K8sClusterState, opts ...pulumi.ResourceOption) (*K8sCluster, error) {
	var resource K8sCluster
	err := ctx.ReadResource("ionoscloud:index/k8sCluster:K8sCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering K8sCluster resources.
type k8sClusterState struct {
	// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the cluster.
	//
	// ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the cluster in order to do it. Set the field to true only if you know what you are doing._**
	AllowReplace *bool `pulumi:"allowReplace"`
	// [list] Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.
	ApiSubnetAllowLists []string `pulumi:"apiSubnetAllowLists"`
	// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
	K8sVersion *string `pulumi:"k8sVersion"`
	// [string] This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have a data center at that location. This property is not adjustable.
	Location *string `pulumi:"location"`
	// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
	MaintenanceWindow *K8sClusterMaintenanceWindow `pulumi:"maintenanceWindow"`
	// [string] The name of the Kubernetes Cluster.
	Name *string `pulumi:"name"`
	// [string] The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the same location as the cluster's location. This attribute is mandatory if the cluster is private.
	NatGatewayIp *string `pulumi:"natGatewayIp"`
	// [string] The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid CIDR notation for an IPv4 network prefix of 16 bits length.
	NodeSubnet *string `pulumi:"nodeSubnet"`
	// [boolean] Indicates if the cluster is public or private. This attribute is immutable.
	Public *bool `pulumi:"public"`
	// [list] List of IONOS Object Storage buckets configured for K8s usage. For now it contains only an IONOS Object Storage bucket used to store K8s API audit logs.
	S3Buckets []K8sClusterS3Bucket `pulumi:"s3Buckets"`
	// [list] List of versions that may be used for node pools under this cluster
	ViableNodePoolVersions []string `pulumi:"viableNodePoolVersions"`
}

type K8sClusterState struct {
	// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the cluster.
	//
	// ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the cluster in order to do it. Set the field to true only if you know what you are doing._**
	AllowReplace pulumi.BoolPtrInput
	// [list] Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.
	ApiSubnetAllowLists pulumi.StringArrayInput
	// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
	K8sVersion pulumi.StringPtrInput
	// [string] This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have a data center at that location. This property is not adjustable.
	Location pulumi.StringPtrInput
	// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
	MaintenanceWindow K8sClusterMaintenanceWindowPtrInput
	// [string] The name of the Kubernetes Cluster.
	Name pulumi.StringPtrInput
	// [string] The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the same location as the cluster's location. This attribute is mandatory if the cluster is private.
	NatGatewayIp pulumi.StringPtrInput
	// [string] The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid CIDR notation for an IPv4 network prefix of 16 bits length.
	NodeSubnet pulumi.StringPtrInput
	// [boolean] Indicates if the cluster is public or private. This attribute is immutable.
	Public pulumi.BoolPtrInput
	// [list] List of IONOS Object Storage buckets configured for K8s usage. For now it contains only an IONOS Object Storage bucket used to store K8s API audit logs.
	S3Buckets K8sClusterS3BucketArrayInput
	// [list] List of versions that may be used for node pools under this cluster
	ViableNodePoolVersions pulumi.StringArrayInput
}

func (K8sClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*k8sClusterState)(nil)).Elem()
}

type k8sClusterArgs struct {
	// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the cluster.
	//
	// ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the cluster in order to do it. Set the field to true only if you know what you are doing._**
	AllowReplace *bool `pulumi:"allowReplace"`
	// [list] Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.
	ApiSubnetAllowLists []string `pulumi:"apiSubnetAllowLists"`
	// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
	K8sVersion *string `pulumi:"k8sVersion"`
	// [string] This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have a data center at that location. This property is not adjustable.
	Location *string `pulumi:"location"`
	// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
	MaintenanceWindow *K8sClusterMaintenanceWindow `pulumi:"maintenanceWindow"`
	// [string] The name of the Kubernetes Cluster.
	Name *string `pulumi:"name"`
	// [string] The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the same location as the cluster's location. This attribute is mandatory if the cluster is private.
	NatGatewayIp *string `pulumi:"natGatewayIp"`
	// [string] The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid CIDR notation for an IPv4 network prefix of 16 bits length.
	NodeSubnet *string `pulumi:"nodeSubnet"`
	// [boolean] Indicates if the cluster is public or private. This attribute is immutable.
	Public *bool `pulumi:"public"`
	// [list] List of IONOS Object Storage buckets configured for K8s usage. For now it contains only an IONOS Object Storage bucket used to store K8s API audit logs.
	S3Buckets []K8sClusterS3Bucket `pulumi:"s3Buckets"`
}

// The set of arguments for constructing a K8sCluster resource.
type K8sClusterArgs struct {
	// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the cluster.
	//
	// ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the cluster in order to do it. Set the field to true only if you know what you are doing._**
	AllowReplace pulumi.BoolPtrInput
	// [list] Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.
	ApiSubnetAllowLists pulumi.StringArrayInput
	// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
	K8sVersion pulumi.StringPtrInput
	// [string] This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have a data center at that location. This property is not adjustable.
	Location pulumi.StringPtrInput
	// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
	MaintenanceWindow K8sClusterMaintenanceWindowPtrInput
	// [string] The name of the Kubernetes Cluster.
	Name pulumi.StringPtrInput
	// [string] The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the same location as the cluster's location. This attribute is mandatory if the cluster is private.
	NatGatewayIp pulumi.StringPtrInput
	// [string] The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid CIDR notation for an IPv4 network prefix of 16 bits length.
	NodeSubnet pulumi.StringPtrInput
	// [boolean] Indicates if the cluster is public or private. This attribute is immutable.
	Public pulumi.BoolPtrInput
	// [list] List of IONOS Object Storage buckets configured for K8s usage. For now it contains only an IONOS Object Storage bucket used to store K8s API audit logs.
	S3Buckets K8sClusterS3BucketArrayInput
}

func (K8sClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*k8sClusterArgs)(nil)).Elem()
}

type K8sClusterInput interface {
	pulumi.Input

	ToK8sClusterOutput() K8sClusterOutput
	ToK8sClusterOutputWithContext(ctx context.Context) K8sClusterOutput
}

func (*K8sCluster) ElementType() reflect.Type {
	return reflect.TypeOf((**K8sCluster)(nil)).Elem()
}

func (i *K8sCluster) ToK8sClusterOutput() K8sClusterOutput {
	return i.ToK8sClusterOutputWithContext(context.Background())
}

func (i *K8sCluster) ToK8sClusterOutputWithContext(ctx context.Context) K8sClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(K8sClusterOutput)
}

// K8sClusterArrayInput is an input type that accepts K8sClusterArray and K8sClusterArrayOutput values.
// You can construct a concrete instance of `K8sClusterArrayInput` via:
//
//	K8sClusterArray{ K8sClusterArgs{...} }
type K8sClusterArrayInput interface {
	pulumi.Input

	ToK8sClusterArrayOutput() K8sClusterArrayOutput
	ToK8sClusterArrayOutputWithContext(context.Context) K8sClusterArrayOutput
}

type K8sClusterArray []K8sClusterInput

func (K8sClusterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*K8sCluster)(nil)).Elem()
}

func (i K8sClusterArray) ToK8sClusterArrayOutput() K8sClusterArrayOutput {
	return i.ToK8sClusterArrayOutputWithContext(context.Background())
}

func (i K8sClusterArray) ToK8sClusterArrayOutputWithContext(ctx context.Context) K8sClusterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(K8sClusterArrayOutput)
}

// K8sClusterMapInput is an input type that accepts K8sClusterMap and K8sClusterMapOutput values.
// You can construct a concrete instance of `K8sClusterMapInput` via:
//
//	K8sClusterMap{ "key": K8sClusterArgs{...} }
type K8sClusterMapInput interface {
	pulumi.Input

	ToK8sClusterMapOutput() K8sClusterMapOutput
	ToK8sClusterMapOutputWithContext(context.Context) K8sClusterMapOutput
}

type K8sClusterMap map[string]K8sClusterInput

func (K8sClusterMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*K8sCluster)(nil)).Elem()
}

func (i K8sClusterMap) ToK8sClusterMapOutput() K8sClusterMapOutput {
	return i.ToK8sClusterMapOutputWithContext(context.Background())
}

func (i K8sClusterMap) ToK8sClusterMapOutputWithContext(ctx context.Context) K8sClusterMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(K8sClusterMapOutput)
}

type K8sClusterOutput struct{ *pulumi.OutputState }

func (K8sClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**K8sCluster)(nil)).Elem()
}

func (o K8sClusterOutput) ToK8sClusterOutput() K8sClusterOutput {
	return o
}

func (o K8sClusterOutput) ToK8sClusterOutputWithContext(ctx context.Context) K8sClusterOutput {
	return o
}

// [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the cluster.
//
// ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the cluster in order to do it. Set the field to true only if you know what you are doing._**
func (o K8sClusterOutput) AllowReplace() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.BoolPtrOutput { return v.AllowReplace }).(pulumi.BoolPtrOutput)
}

// [list] Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.
func (o K8sClusterOutput) ApiSubnetAllowLists() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.StringArrayOutput { return v.ApiSubnetAllowLists }).(pulumi.StringArrayOutput)
}

// [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
func (o K8sClusterOutput) K8sVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.StringOutput { return v.K8sVersion }).(pulumi.StringOutput)
}

// [string] This attribute is mandatory if the cluster is private. The location must be enabled for your contract, or you must have a data center at that location. This property is not adjustable.
func (o K8sClusterOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.StringPtrOutput { return v.Location }).(pulumi.StringPtrOutput)
}

// A maintenance window comprise of a day of the week and a time for maintenance to be allowed
func (o K8sClusterOutput) MaintenanceWindow() K8sClusterMaintenanceWindowOutput {
	return o.ApplyT(func(v *K8sCluster) K8sClusterMaintenanceWindowOutput { return v.MaintenanceWindow }).(K8sClusterMaintenanceWindowOutput)
}

// [string] The name of the Kubernetes Cluster.
func (o K8sClusterOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [string] The NAT gateway IP of the cluster if the cluster is private. This attribute is immutable. Must be a reserved IP in the same location as the cluster's location. This attribute is mandatory if the cluster is private.
func (o K8sClusterOutput) NatGatewayIp() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.StringPtrOutput { return v.NatGatewayIp }).(pulumi.StringPtrOutput)
}

// [string] The node subnet of the cluster, if the cluster is private. This attribute is optional and immutable. Must be a valid CIDR notation for an IPv4 network prefix of 16 bits length.
func (o K8sClusterOutput) NodeSubnet() pulumi.StringOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.StringOutput { return v.NodeSubnet }).(pulumi.StringOutput)
}

// [boolean] Indicates if the cluster is public or private. This attribute is immutable.
func (o K8sClusterOutput) Public() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.BoolPtrOutput { return v.Public }).(pulumi.BoolPtrOutput)
}

// [list] List of IONOS Object Storage buckets configured for K8s usage. For now it contains only an IONOS Object Storage bucket used to store K8s API audit logs.
func (o K8sClusterOutput) S3Buckets() K8sClusterS3BucketArrayOutput {
	return o.ApplyT(func(v *K8sCluster) K8sClusterS3BucketArrayOutput { return v.S3Buckets }).(K8sClusterS3BucketArrayOutput)
}

// [list] List of versions that may be used for node pools under this cluster
func (o K8sClusterOutput) ViableNodePoolVersions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *K8sCluster) pulumi.StringArrayOutput { return v.ViableNodePoolVersions }).(pulumi.StringArrayOutput)
}

type K8sClusterArrayOutput struct{ *pulumi.OutputState }

func (K8sClusterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*K8sCluster)(nil)).Elem()
}

func (o K8sClusterArrayOutput) ToK8sClusterArrayOutput() K8sClusterArrayOutput {
	return o
}

func (o K8sClusterArrayOutput) ToK8sClusterArrayOutputWithContext(ctx context.Context) K8sClusterArrayOutput {
	return o
}

func (o K8sClusterArrayOutput) Index(i pulumi.IntInput) K8sClusterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *K8sCluster {
		return vs[0].([]*K8sCluster)[vs[1].(int)]
	}).(K8sClusterOutput)
}

type K8sClusterMapOutput struct{ *pulumi.OutputState }

func (K8sClusterMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*K8sCluster)(nil)).Elem()
}

func (o K8sClusterMapOutput) ToK8sClusterMapOutput() K8sClusterMapOutput {
	return o
}

func (o K8sClusterMapOutput) ToK8sClusterMapOutputWithContext(ctx context.Context) K8sClusterMapOutput {
	return o
}

func (o K8sClusterMapOutput) MapIndex(k pulumi.StringInput) K8sClusterOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *K8sCluster {
		return vs[0].(map[string]*K8sCluster)[vs[1].(string)]
	}).(K8sClusterOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*K8sClusterInput)(nil)).Elem(), &K8sCluster{})
	pulumi.RegisterInputType(reflect.TypeOf((*K8sClusterArrayInput)(nil)).Elem(), K8sClusterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*K8sClusterMapInput)(nil)).Elem(), K8sClusterMap{})
	pulumi.RegisterOutputType(K8sClusterOutput{})
	pulumi.RegisterOutputType(K8sClusterArrayOutput{})
	pulumi.RegisterOutputType(K8sClusterMapOutput{})
}

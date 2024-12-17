// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **DbaaS Mongo Cluster data source** can be used to search for and return an existing DbaaS MongoDB Cluster.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
func LookupMongoCluster(ctx *pulumi.Context, args *LookupMongoClusterArgs, opts ...pulumi.InvokeOption) (*LookupMongoClusterResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMongoClusterResult
	err := ctx.Invoke("ionoscloud:dbaas/getMongoCluster:getMongoCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getMongoCluster.
type LookupMongoClusterArgs struct {
	// The name of your cluster. Updates to the value of the field force the cluster to be re-created.
	DisplayName *string `pulumi:"displayName"`
	Id          *string `pulumi:"id"`
}

// A collection of values returned by getMongoCluster.
type LookupMongoClusterResult struct {
	Backups      []GetMongoClusterBackup      `pulumi:"backups"`
	BiConnectors []GetMongoClusterBiConnector `pulumi:"biConnectors"`
	// The physical location where the cluster will be created. This will be where all of your instances live. Updates to the value of the field force the cluster to be re-created. Available locations: de/txl, gb/lhr, es/vit"
	ConnectionString string `pulumi:"connectionString"`
	// Details about the network connection for your cluster. Updates to the value of the field force the cluster to be re-created.
	Connections []GetMongoClusterConnection `pulumi:"connections"`
	// The number of CPU cores per replica. Required for enterprise edition.
	Cores int `pulumi:"cores"`
	// The name of your cluster. Updates to the value of the field force the cluster to be re-created.
	DisplayName *string `pulumi:"displayName"`
	// Cluster edition. Playground, business or enterprise.
	Edition string  `pulumi:"edition"`
	Id      *string `pulumi:"id"`
	// The total number of instances in the cluster (one master and n-1 standbys). Example: 3, 5, 7. Updates to the value of the field force the cluster to be re-created.
	Instances int `pulumi:"instances"`
	// The location where the cluster backups will be stored. If not set, the backup is stored in the nearest location of the cluster. Possible values are de, eu-south-2, or eu-central-2.
	Location string `pulumi:"location"`
	// A weekly 4 hour-long window, during which maintenance might occur.  Updates to the value of the field force the cluster to be re-created.
	MaintenanceWindows []GetMongoClusterMaintenanceWindow `pulumi:"maintenanceWindows"`
	// The MongoDB version of your cluster. Updates to the value of the field force the cluster to be re-created.
	MongodbVersion string `pulumi:"mongodbVersion"`
	// The amount of memory per instance in megabytes. Required for enterprise edition.
	Ram    int `pulumi:"ram"`
	Shards int `pulumi:"shards"`
	// The amount of storage per instance in MB. Required for enterprise edition.
	StorageSize int `pulumi:"storageSize"`
	// The storage type used in your cluster. Required for enterprise edition.
	StorageType string `pulumi:"storageType"`
	// The unique ID of the template, which specifies the number of cores, storage size, and memory. Updates to the value of the field force the cluster to be re-created.
	TemplateId string `pulumi:"templateId"`
	Type       string `pulumi:"type"`
}

func LookupMongoClusterOutput(ctx *pulumi.Context, args LookupMongoClusterOutputArgs, opts ...pulumi.InvokeOption) LookupMongoClusterResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupMongoClusterResultOutput, error) {
			args := v.(LookupMongoClusterArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:dbaas/getMongoCluster:getMongoCluster", args, LookupMongoClusterResultOutput{}, options).(LookupMongoClusterResultOutput), nil
		}).(LookupMongoClusterResultOutput)
}

// A collection of arguments for invoking getMongoCluster.
type LookupMongoClusterOutputArgs struct {
	// The name of your cluster. Updates to the value of the field force the cluster to be re-created.
	DisplayName pulumi.StringPtrInput `pulumi:"displayName"`
	Id          pulumi.StringPtrInput `pulumi:"id"`
}

func (LookupMongoClusterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMongoClusterArgs)(nil)).Elem()
}

// A collection of values returned by getMongoCluster.
type LookupMongoClusterResultOutput struct{ *pulumi.OutputState }

func (LookupMongoClusterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMongoClusterResult)(nil)).Elem()
}

func (o LookupMongoClusterResultOutput) ToLookupMongoClusterResultOutput() LookupMongoClusterResultOutput {
	return o
}

func (o LookupMongoClusterResultOutput) ToLookupMongoClusterResultOutputWithContext(ctx context.Context) LookupMongoClusterResultOutput {
	return o
}

func (o LookupMongoClusterResultOutput) Backups() GetMongoClusterBackupArrayOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) []GetMongoClusterBackup { return v.Backups }).(GetMongoClusterBackupArrayOutput)
}

func (o LookupMongoClusterResultOutput) BiConnectors() GetMongoClusterBiConnectorArrayOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) []GetMongoClusterBiConnector { return v.BiConnectors }).(GetMongoClusterBiConnectorArrayOutput)
}

// The physical location where the cluster will be created. This will be where all of your instances live. Updates to the value of the field force the cluster to be re-created. Available locations: de/txl, gb/lhr, es/vit"
func (o LookupMongoClusterResultOutput) ConnectionString() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) string { return v.ConnectionString }).(pulumi.StringOutput)
}

// Details about the network connection for your cluster. Updates to the value of the field force the cluster to be re-created.
func (o LookupMongoClusterResultOutput) Connections() GetMongoClusterConnectionArrayOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) []GetMongoClusterConnection { return v.Connections }).(GetMongoClusterConnectionArrayOutput)
}

// The number of CPU cores per replica. Required for enterprise edition.
func (o LookupMongoClusterResultOutput) Cores() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) int { return v.Cores }).(pulumi.IntOutput)
}

// The name of your cluster. Updates to the value of the field force the cluster to be re-created.
func (o LookupMongoClusterResultOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) *string { return v.DisplayName }).(pulumi.StringPtrOutput)
}

// Cluster edition. Playground, business or enterprise.
func (o LookupMongoClusterResultOutput) Edition() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) string { return v.Edition }).(pulumi.StringOutput)
}

func (o LookupMongoClusterResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The total number of instances in the cluster (one master and n-1 standbys). Example: 3, 5, 7. Updates to the value of the field force the cluster to be re-created.
func (o LookupMongoClusterResultOutput) Instances() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) int { return v.Instances }).(pulumi.IntOutput)
}

// The location where the cluster backups will be stored. If not set, the backup is stored in the nearest location of the cluster. Possible values are de, eu-south-2, or eu-central-2.
func (o LookupMongoClusterResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) string { return v.Location }).(pulumi.StringOutput)
}

// A weekly 4 hour-long window, during which maintenance might occur.  Updates to the value of the field force the cluster to be re-created.
func (o LookupMongoClusterResultOutput) MaintenanceWindows() GetMongoClusterMaintenanceWindowArrayOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) []GetMongoClusterMaintenanceWindow { return v.MaintenanceWindows }).(GetMongoClusterMaintenanceWindowArrayOutput)
}

// The MongoDB version of your cluster. Updates to the value of the field force the cluster to be re-created.
func (o LookupMongoClusterResultOutput) MongodbVersion() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) string { return v.MongodbVersion }).(pulumi.StringOutput)
}

// The amount of memory per instance in megabytes. Required for enterprise edition.
func (o LookupMongoClusterResultOutput) Ram() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) int { return v.Ram }).(pulumi.IntOutput)
}

func (o LookupMongoClusterResultOutput) Shards() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) int { return v.Shards }).(pulumi.IntOutput)
}

// The amount of storage per instance in MB. Required for enterprise edition.
func (o LookupMongoClusterResultOutput) StorageSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) int { return v.StorageSize }).(pulumi.IntOutput)
}

// The storage type used in your cluster. Required for enterprise edition.
func (o LookupMongoClusterResultOutput) StorageType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) string { return v.StorageType }).(pulumi.StringOutput)
}

// The unique ID of the template, which specifies the number of cores, storage size, and memory. Updates to the value of the field force the cluster to be re-created.
func (o LookupMongoClusterResultOutput) TemplateId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) string { return v.TemplateId }).(pulumi.StringOutput)
}

func (o LookupMongoClusterResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoClusterResult) string { return v.Type }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMongoClusterResultOutput{})
}

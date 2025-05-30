// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **DBaaS MariaDB Cluster data source** can be used to search for and return an existing DBaaS MariaDB Cluster.
//
// ## Example Usage
//
// ### By ID
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dbaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dbaas.LookupMariaDBCluster(ctx, &dbaas.LookupMariaDBClusterArgs{
//				Id:       pulumi.StringRef("cluster_id"),
//				Location: pulumi.StringRef("de/txl"),
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
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dbaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dbaas.LookupMariaDBCluster(ctx, &dbaas.LookupMariaDBClusterArgs{
//				DisplayName: pulumi.StringRef("MariaDB_cluster"),
//				Location:    pulumi.StringRef("de/txl"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupMariaDBCluster(ctx *pulumi.Context, args *LookupMariaDBClusterArgs, opts ...pulumi.InvokeOption) (*LookupMariaDBClusterResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMariaDBClusterResult
	err := ctx.Invoke("ionoscloud:dbaas/getMariaDBCluster:getMariaDBCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getMariaDBCluster.
type LookupMariaDBClusterArgs struct {
	// [string] Display Name of an existing cluster that you want to search for.
	DisplayName *string `pulumi:"displayName"`
	// [string] ID of the cluster you want to search for.
	Id *string `pulumi:"id"`
	// [string] The location of the cluster. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
	//
	// > **⚠ WARNING:** `Location` attribute will become required in the future.
	//
	// Either `displayName` or `id` must be provided. If none or both are provided, the datasource will return an error.
	Location *string `pulumi:"location"`
}

// A collection of values returned by getMariaDBCluster.
type LookupMariaDBClusterResult struct {
	// The network connection for your cluster. Only one connection is allowed.
	Connections []GetMariaDBClusterConnection `pulumi:"connections"`
	// [int] The number of CPU cores per instance.
	Cores int `pulumi:"cores"`
	// [string] The friendly name of your cluster.
	DisplayName string `pulumi:"displayName"`
	// [string] The DNS name pointing to your cluster.
	DnsName string `pulumi:"dnsName"`
	Id      string `pulumi:"id"`
	// [int] The total number of instances in the cluster (one primary and n-1 secondary).
	Instances int     `pulumi:"instances"`
	Location  *string `pulumi:"location"`
	// A weekly 4 hour-long window, during which maintenance might occur.
	MaintenanceWindows []GetMariaDBClusterMaintenanceWindow `pulumi:"maintenanceWindows"`
	// [string] The MariaDB version of your cluster.
	MariadbVersion string `pulumi:"mariadbVersion"`
	// [int] The amount of memory per instance in gigabytes (GB).
	Ram int `pulumi:"ram"`
	// [int] The amount of storage per instance in gigabytes (GB).
	StorageSize int `pulumi:"storageSize"`
}

func LookupMariaDBClusterOutput(ctx *pulumi.Context, args LookupMariaDBClusterOutputArgs, opts ...pulumi.InvokeOption) LookupMariaDBClusterResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupMariaDBClusterResultOutput, error) {
			args := v.(LookupMariaDBClusterArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:dbaas/getMariaDBCluster:getMariaDBCluster", args, LookupMariaDBClusterResultOutput{}, options).(LookupMariaDBClusterResultOutput), nil
		}).(LookupMariaDBClusterResultOutput)
}

// A collection of arguments for invoking getMariaDBCluster.
type LookupMariaDBClusterOutputArgs struct {
	// [string] Display Name of an existing cluster that you want to search for.
	DisplayName pulumi.StringPtrInput `pulumi:"displayName"`
	// [string] ID of the cluster you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// [string] The location of the cluster. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
	//
	// > **⚠ WARNING:** `Location` attribute will become required in the future.
	//
	// Either `displayName` or `id` must be provided. If none or both are provided, the datasource will return an error.
	Location pulumi.StringPtrInput `pulumi:"location"`
}

func (LookupMariaDBClusterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMariaDBClusterArgs)(nil)).Elem()
}

// A collection of values returned by getMariaDBCluster.
type LookupMariaDBClusterResultOutput struct{ *pulumi.OutputState }

func (LookupMariaDBClusterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMariaDBClusterResult)(nil)).Elem()
}

func (o LookupMariaDBClusterResultOutput) ToLookupMariaDBClusterResultOutput() LookupMariaDBClusterResultOutput {
	return o
}

func (o LookupMariaDBClusterResultOutput) ToLookupMariaDBClusterResultOutputWithContext(ctx context.Context) LookupMariaDBClusterResultOutput {
	return o
}

// The network connection for your cluster. Only one connection is allowed.
func (o LookupMariaDBClusterResultOutput) Connections() GetMariaDBClusterConnectionArrayOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) []GetMariaDBClusterConnection { return v.Connections }).(GetMariaDBClusterConnectionArrayOutput)
}

// [int] The number of CPU cores per instance.
func (o LookupMariaDBClusterResultOutput) Cores() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) int { return v.Cores }).(pulumi.IntOutput)
}

// [string] The friendly name of your cluster.
func (o LookupMariaDBClusterResultOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) string { return v.DisplayName }).(pulumi.StringOutput)
}

// [string] The DNS name pointing to your cluster.
func (o LookupMariaDBClusterResultOutput) DnsName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) string { return v.DnsName }).(pulumi.StringOutput)
}

func (o LookupMariaDBClusterResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) string { return v.Id }).(pulumi.StringOutput)
}

// [int] The total number of instances in the cluster (one primary and n-1 secondary).
func (o LookupMariaDBClusterResultOutput) Instances() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) int { return v.Instances }).(pulumi.IntOutput)
}

func (o LookupMariaDBClusterResultOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) *string { return v.Location }).(pulumi.StringPtrOutput)
}

// A weekly 4 hour-long window, during which maintenance might occur.
func (o LookupMariaDBClusterResultOutput) MaintenanceWindows() GetMariaDBClusterMaintenanceWindowArrayOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) []GetMariaDBClusterMaintenanceWindow { return v.MaintenanceWindows }).(GetMariaDBClusterMaintenanceWindowArrayOutput)
}

// [string] The MariaDB version of your cluster.
func (o LookupMariaDBClusterResultOutput) MariadbVersion() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) string { return v.MariadbVersion }).(pulumi.StringOutput)
}

// [int] The amount of memory per instance in gigabytes (GB).
func (o LookupMariaDBClusterResultOutput) Ram() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) int { return v.Ram }).(pulumi.IntOutput)
}

// [int] The amount of storage per instance in gigabytes (GB).
func (o LookupMariaDBClusterResultOutput) StorageSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupMariaDBClusterResult) int { return v.StorageSize }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMariaDBClusterResultOutput{})
}

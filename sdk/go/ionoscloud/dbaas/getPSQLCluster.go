// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupPSQLCluster(ctx *pulumi.Context, args *LookupPSQLClusterArgs, opts ...pulumi.InvokeOption) (*LookupPSQLClusterResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPSQLClusterResult
	err := ctx.Invoke("ionoscloud:dbaas/getPSQLCluster:getPSQLCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPSQLCluster.
type LookupPSQLClusterArgs struct {
	DisplayName *string `pulumi:"displayName"`
	Id          *string `pulumi:"id"`
}

// A collection of values returned by getPSQLCluster.
type LookupPSQLClusterResult struct {
	BackupLocation      string                            `pulumi:"backupLocation"`
	ConnectionPoolers   []GetPSQLClusterConnectionPooler  `pulumi:"connectionPoolers"`
	Connections         []GetPSQLClusterConnection        `pulumi:"connections"`
	Cores               int                               `pulumi:"cores"`
	DisplayName         *string                           `pulumi:"displayName"`
	DnsName             string                            `pulumi:"dnsName"`
	FromBackups         []GetPSQLClusterFromBackup        `pulumi:"fromBackups"`
	Id                  *string                           `pulumi:"id"`
	Instances           int                               `pulumi:"instances"`
	Location            string                            `pulumi:"location"`
	MaintenanceWindows  []GetPSQLClusterMaintenanceWindow `pulumi:"maintenanceWindows"`
	PostgresVersion     string                            `pulumi:"postgresVersion"`
	Ram                 int                               `pulumi:"ram"`
	StorageSize         int                               `pulumi:"storageSize"`
	StorageType         string                            `pulumi:"storageType"`
	SynchronizationMode string                            `pulumi:"synchronizationMode"`
}

func LookupPSQLClusterOutput(ctx *pulumi.Context, args LookupPSQLClusterOutputArgs, opts ...pulumi.InvokeOption) LookupPSQLClusterResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupPSQLClusterResultOutput, error) {
			args := v.(LookupPSQLClusterArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:dbaas/getPSQLCluster:getPSQLCluster", args, LookupPSQLClusterResultOutput{}, options).(LookupPSQLClusterResultOutput), nil
		}).(LookupPSQLClusterResultOutput)
}

// A collection of arguments for invoking getPSQLCluster.
type LookupPSQLClusterOutputArgs struct {
	DisplayName pulumi.StringPtrInput `pulumi:"displayName"`
	Id          pulumi.StringPtrInput `pulumi:"id"`
}

func (LookupPSQLClusterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPSQLClusterArgs)(nil)).Elem()
}

// A collection of values returned by getPSQLCluster.
type LookupPSQLClusterResultOutput struct{ *pulumi.OutputState }

func (LookupPSQLClusterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPSQLClusterResult)(nil)).Elem()
}

func (o LookupPSQLClusterResultOutput) ToLookupPSQLClusterResultOutput() LookupPSQLClusterResultOutput {
	return o
}

func (o LookupPSQLClusterResultOutput) ToLookupPSQLClusterResultOutputWithContext(ctx context.Context) LookupPSQLClusterResultOutput {
	return o
}

func (o LookupPSQLClusterResultOutput) BackupLocation() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) string { return v.BackupLocation }).(pulumi.StringOutput)
}

func (o LookupPSQLClusterResultOutput) ConnectionPoolers() GetPSQLClusterConnectionPoolerArrayOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) []GetPSQLClusterConnectionPooler { return v.ConnectionPoolers }).(GetPSQLClusterConnectionPoolerArrayOutput)
}

func (o LookupPSQLClusterResultOutput) Connections() GetPSQLClusterConnectionArrayOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) []GetPSQLClusterConnection { return v.Connections }).(GetPSQLClusterConnectionArrayOutput)
}

func (o LookupPSQLClusterResultOutput) Cores() pulumi.IntOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) int { return v.Cores }).(pulumi.IntOutput)
}

func (o LookupPSQLClusterResultOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) *string { return v.DisplayName }).(pulumi.StringPtrOutput)
}

func (o LookupPSQLClusterResultOutput) DnsName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) string { return v.DnsName }).(pulumi.StringOutput)
}

func (o LookupPSQLClusterResultOutput) FromBackups() GetPSQLClusterFromBackupArrayOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) []GetPSQLClusterFromBackup { return v.FromBackups }).(GetPSQLClusterFromBackupArrayOutput)
}

func (o LookupPSQLClusterResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupPSQLClusterResultOutput) Instances() pulumi.IntOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) int { return v.Instances }).(pulumi.IntOutput)
}

func (o LookupPSQLClusterResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) string { return v.Location }).(pulumi.StringOutput)
}

func (o LookupPSQLClusterResultOutput) MaintenanceWindows() GetPSQLClusterMaintenanceWindowArrayOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) []GetPSQLClusterMaintenanceWindow { return v.MaintenanceWindows }).(GetPSQLClusterMaintenanceWindowArrayOutput)
}

func (o LookupPSQLClusterResultOutput) PostgresVersion() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) string { return v.PostgresVersion }).(pulumi.StringOutput)
}

func (o LookupPSQLClusterResultOutput) Ram() pulumi.IntOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) int { return v.Ram }).(pulumi.IntOutput)
}

func (o LookupPSQLClusterResultOutput) StorageSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) int { return v.StorageSize }).(pulumi.IntOutput)
}

func (o LookupPSQLClusterResultOutput) StorageType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) string { return v.StorageType }).(pulumi.StringOutput)
}

func (o LookupPSQLClusterResultOutput) SynchronizationMode() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPSQLClusterResult) string { return v.SynchronizationMode }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPSQLClusterResultOutput{})
}

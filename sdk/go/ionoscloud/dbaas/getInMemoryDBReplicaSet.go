// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupInMemoryDBReplicaSet(ctx *pulumi.Context, args *LookupInMemoryDBReplicaSetArgs, opts ...pulumi.InvokeOption) (*LookupInMemoryDBReplicaSetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupInMemoryDBReplicaSetResult
	err := ctx.Invoke("ionoscloud:dbaas/getInMemoryDBReplicaSet:getInMemoryDBReplicaSet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getInMemoryDBReplicaSet.
type LookupInMemoryDBReplicaSetArgs struct {
	DisplayName *string `pulumi:"displayName"`
	Id          *string `pulumi:"id"`
	Location    string  `pulumi:"location"`
}

// A collection of values returned by getInMemoryDBReplicaSet.
type LookupInMemoryDBReplicaSetResult struct {
	Connections        []GetInMemoryDBReplicaSetConnection        `pulumi:"connections"`
	Credentials        []GetInMemoryDBReplicaSetCredential        `pulumi:"credentials"`
	DisplayName        *string                                    `pulumi:"displayName"`
	DnsName            string                                     `pulumi:"dnsName"`
	EvictionPolicy     string                                     `pulumi:"evictionPolicy"`
	Id                 *string                                    `pulumi:"id"`
	Location           string                                     `pulumi:"location"`
	MaintenanceWindows []GetInMemoryDBReplicaSetMaintenanceWindow `pulumi:"maintenanceWindows"`
	PersistenceMode    string                                     `pulumi:"persistenceMode"`
	Replicas           int                                        `pulumi:"replicas"`
	Resources          []GetInMemoryDBReplicaSetResource          `pulumi:"resources"`
	Version            string                                     `pulumi:"version"`
}

func LookupInMemoryDBReplicaSetOutput(ctx *pulumi.Context, args LookupInMemoryDBReplicaSetOutputArgs, opts ...pulumi.InvokeOption) LookupInMemoryDBReplicaSetResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupInMemoryDBReplicaSetResultOutput, error) {
			args := v.(LookupInMemoryDBReplicaSetArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:dbaas/getInMemoryDBReplicaSet:getInMemoryDBReplicaSet", args, LookupInMemoryDBReplicaSetResultOutput{}, options).(LookupInMemoryDBReplicaSetResultOutput), nil
		}).(LookupInMemoryDBReplicaSetResultOutput)
}

// A collection of arguments for invoking getInMemoryDBReplicaSet.
type LookupInMemoryDBReplicaSetOutputArgs struct {
	DisplayName pulumi.StringPtrInput `pulumi:"displayName"`
	Id          pulumi.StringPtrInput `pulumi:"id"`
	Location    pulumi.StringInput    `pulumi:"location"`
}

func (LookupInMemoryDBReplicaSetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInMemoryDBReplicaSetArgs)(nil)).Elem()
}

// A collection of values returned by getInMemoryDBReplicaSet.
type LookupInMemoryDBReplicaSetResultOutput struct{ *pulumi.OutputState }

func (LookupInMemoryDBReplicaSetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInMemoryDBReplicaSetResult)(nil)).Elem()
}

func (o LookupInMemoryDBReplicaSetResultOutput) ToLookupInMemoryDBReplicaSetResultOutput() LookupInMemoryDBReplicaSetResultOutput {
	return o
}

func (o LookupInMemoryDBReplicaSetResultOutput) ToLookupInMemoryDBReplicaSetResultOutputWithContext(ctx context.Context) LookupInMemoryDBReplicaSetResultOutput {
	return o
}

func (o LookupInMemoryDBReplicaSetResultOutput) Connections() GetInMemoryDBReplicaSetConnectionArrayOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) []GetInMemoryDBReplicaSetConnection { return v.Connections }).(GetInMemoryDBReplicaSetConnectionArrayOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) Credentials() GetInMemoryDBReplicaSetCredentialArrayOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) []GetInMemoryDBReplicaSetCredential { return v.Credentials }).(GetInMemoryDBReplicaSetCredentialArrayOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) *string { return v.DisplayName }).(pulumi.StringPtrOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) DnsName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) string { return v.DnsName }).(pulumi.StringOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) EvictionPolicy() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) string { return v.EvictionPolicy }).(pulumi.StringOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) string { return v.Location }).(pulumi.StringOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) MaintenanceWindows() GetInMemoryDBReplicaSetMaintenanceWindowArrayOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) []GetInMemoryDBReplicaSetMaintenanceWindow {
		return v.MaintenanceWindows
	}).(GetInMemoryDBReplicaSetMaintenanceWindowArrayOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) PersistenceMode() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) string { return v.PersistenceMode }).(pulumi.StringOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) Replicas() pulumi.IntOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) int { return v.Replicas }).(pulumi.IntOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) Resources() GetInMemoryDBReplicaSetResourceArrayOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) []GetInMemoryDBReplicaSetResource { return v.Resources }).(GetInMemoryDBReplicaSetResourceArrayOutput)
}

func (o LookupInMemoryDBReplicaSetResultOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInMemoryDBReplicaSetResult) string { return v.Version }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupInMemoryDBReplicaSetResultOutput{})
}

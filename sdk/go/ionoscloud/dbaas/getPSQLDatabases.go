// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **PgSql Databases data source** can be used to search for and return multiple existing PgSql databases.
//
// ## Example Usage
//
// ### All databases from a specific cluster
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
//			_, err := dbaas.GetPSQLDatabases(ctx, &dbaas.GetPSQLDatabasesArgs{
//				ClusterId: "cluster_id",
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
// ### Filter by owner
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
//			_, err := dbaas.GetPSQLDatabases(ctx, &dbaas.GetPSQLDatabasesArgs{
//				ClusterId: "cluster_id",
//				Owner:     pulumi.StringRef("owner"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetPSQLDatabases(ctx *pulumi.Context, args *GetPSQLDatabasesArgs, opts ...pulumi.InvokeOption) (*GetPSQLDatabasesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetPSQLDatabasesResult
	err := ctx.Invoke("ionoscloud:dbaas/getPSQLDatabases:getPSQLDatabases", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPSQLDatabases.
type GetPSQLDatabasesArgs struct {
	// [string] The ID of the cluster.
	ClusterId string `pulumi:"clusterId"`
	// [string] Filter using a specific owner.
	Owner *string `pulumi:"owner"`
}

// A collection of values returned by getPSQLDatabases.
type GetPSQLDatabasesResult struct {
	ClusterId string `pulumi:"clusterId"`
	// [list] A list that contains either all databases, either some of them (filter by owner). A database from list has the following format:
	Databases []GetPSQLDatabasesDatabase `pulumi:"databases"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// [string] The owner of the database.
	Owner *string `pulumi:"owner"`
}

func GetPSQLDatabasesOutput(ctx *pulumi.Context, args GetPSQLDatabasesOutputArgs, opts ...pulumi.InvokeOption) GetPSQLDatabasesResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetPSQLDatabasesResultOutput, error) {
			args := v.(GetPSQLDatabasesArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:dbaas/getPSQLDatabases:getPSQLDatabases", args, GetPSQLDatabasesResultOutput{}, options).(GetPSQLDatabasesResultOutput), nil
		}).(GetPSQLDatabasesResultOutput)
}

// A collection of arguments for invoking getPSQLDatabases.
type GetPSQLDatabasesOutputArgs struct {
	// [string] The ID of the cluster.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// [string] Filter using a specific owner.
	Owner pulumi.StringPtrInput `pulumi:"owner"`
}

func (GetPSQLDatabasesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPSQLDatabasesArgs)(nil)).Elem()
}

// A collection of values returned by getPSQLDatabases.
type GetPSQLDatabasesResultOutput struct{ *pulumi.OutputState }

func (GetPSQLDatabasesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPSQLDatabasesResult)(nil)).Elem()
}

func (o GetPSQLDatabasesResultOutput) ToGetPSQLDatabasesResultOutput() GetPSQLDatabasesResultOutput {
	return o
}

func (o GetPSQLDatabasesResultOutput) ToGetPSQLDatabasesResultOutputWithContext(ctx context.Context) GetPSQLDatabasesResultOutput {
	return o
}

func (o GetPSQLDatabasesResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetPSQLDatabasesResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// [list] A list that contains either all databases, either some of them (filter by owner). A database from list has the following format:
func (o GetPSQLDatabasesResultOutput) Databases() GetPSQLDatabasesDatabaseArrayOutput {
	return o.ApplyT(func(v GetPSQLDatabasesResult) []GetPSQLDatabasesDatabase { return v.Databases }).(GetPSQLDatabasesDatabaseArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetPSQLDatabasesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPSQLDatabasesResult) string { return v.Id }).(pulumi.StringOutput)
}

// [string] The owner of the database.
func (o GetPSQLDatabasesResultOutput) Owner() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPSQLDatabasesResult) *string { return v.Owner }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPSQLDatabasesResultOutput{})
}

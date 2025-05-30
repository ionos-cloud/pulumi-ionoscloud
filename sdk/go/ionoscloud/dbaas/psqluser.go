// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **DbaaS PgSql User**.
//
// ## Example Usage
//
// Create a `PgSQL` cluster as presented in the documentation for the cluster, then define a user resource
// and link it with the previously created cluster:
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dbaas"
//	"github.com/pulumi/pulumi-random/sdk/go/random"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			userPassword, err := random.NewPassword(ctx, "user_password", &random.PasswordArgs{
//				Length:          16,
//				Special:         true,
//				OverrideSpecial: "!#$%&*()-_=+[]{}<>:?",
//			})
//			if err != nil {
//				return err
//			}
//			_, err = dbaas.NewPSQLUser(ctx, "example_pg_user", &dbaas.PSQLUserArgs{
//				ClusterId: pulumi.Any(example.Id),
//				Username:  pulumi.String("exampleuser"),
//				Password:  userPassword.Result,
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// In order to import a PgSql user, you can define an empty user resource in the plan:
//
// hcl
//
// resource "ionoscloud_pg_user" "example" {
//
// }
//
// The resource can be imported using the `clusterId` and the `username`, for example:
//
// ```sh
// $ pulumi import ionoscloud:dbaas/pSQLUser:PSQLUser example clusterid/username
// ```
type PSQLUser struct {
	pulumi.CustomResourceState

	// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// [bool] Describes whether this user is a system user or not. A system user cannot be updated or deleted.
	IsSystemUser pulumi.BoolOutput `pulumi:"isSystemUser"`
	// [string] User password.
	Password pulumi.StringOutput `pulumi:"password"`
	// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
	Username pulumi.StringOutput `pulumi:"username"`
}

// NewPSQLUser registers a new resource with the given unique name, arguments, and options.
func NewPSQLUser(ctx *pulumi.Context,
	name string, args *PSQLUserArgs, opts ...pulumi.ResourceOption) (*PSQLUser, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	if args.Password == nil {
		return nil, errors.New("invalid value for required argument 'Password'")
	}
	if args.Username == nil {
		return nil, errors.New("invalid value for required argument 'Username'")
	}
	if args.Password != nil {
		args.Password = pulumi.ToSecret(args.Password).(pulumi.StringInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"password",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource PSQLUser
	err := ctx.RegisterResource("ionoscloud:dbaas/pSQLUser:PSQLUser", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPSQLUser gets an existing PSQLUser resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPSQLUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PSQLUserState, opts ...pulumi.ResourceOption) (*PSQLUser, error) {
	var resource PSQLUser
	err := ctx.ReadResource("ionoscloud:dbaas/pSQLUser:PSQLUser", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PSQLUser resources.
type psqluserState struct {
	// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
	ClusterId *string `pulumi:"clusterId"`
	// [bool] Describes whether this user is a system user or not. A system user cannot be updated or deleted.
	IsSystemUser *bool `pulumi:"isSystemUser"`
	// [string] User password.
	Password *string `pulumi:"password"`
	// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
	Username *string `pulumi:"username"`
}

type PSQLUserState struct {
	// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
	ClusterId pulumi.StringPtrInput
	// [bool] Describes whether this user is a system user or not. A system user cannot be updated or deleted.
	IsSystemUser pulumi.BoolPtrInput
	// [string] User password.
	Password pulumi.StringPtrInput
	// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
	Username pulumi.StringPtrInput
}

func (PSQLUserState) ElementType() reflect.Type {
	return reflect.TypeOf((*psqluserState)(nil)).Elem()
}

type psqluserArgs struct {
	// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
	ClusterId string `pulumi:"clusterId"`
	// [string] User password.
	Password string `pulumi:"password"`
	// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
	Username string `pulumi:"username"`
}

// The set of arguments for constructing a PSQLUser resource.
type PSQLUserArgs struct {
	// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
	ClusterId pulumi.StringInput
	// [string] User password.
	Password pulumi.StringInput
	// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
	Username pulumi.StringInput
}

func (PSQLUserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*psqluserArgs)(nil)).Elem()
}

type PSQLUserInput interface {
	pulumi.Input

	ToPSQLUserOutput() PSQLUserOutput
	ToPSQLUserOutputWithContext(ctx context.Context) PSQLUserOutput
}

func (*PSQLUser) ElementType() reflect.Type {
	return reflect.TypeOf((**PSQLUser)(nil)).Elem()
}

func (i *PSQLUser) ToPSQLUserOutput() PSQLUserOutput {
	return i.ToPSQLUserOutputWithContext(context.Background())
}

func (i *PSQLUser) ToPSQLUserOutputWithContext(ctx context.Context) PSQLUserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PSQLUserOutput)
}

// PSQLUserArrayInput is an input type that accepts PSQLUserArray and PSQLUserArrayOutput values.
// You can construct a concrete instance of `PSQLUserArrayInput` via:
//
//	PSQLUserArray{ PSQLUserArgs{...} }
type PSQLUserArrayInput interface {
	pulumi.Input

	ToPSQLUserArrayOutput() PSQLUserArrayOutput
	ToPSQLUserArrayOutputWithContext(context.Context) PSQLUserArrayOutput
}

type PSQLUserArray []PSQLUserInput

func (PSQLUserArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PSQLUser)(nil)).Elem()
}

func (i PSQLUserArray) ToPSQLUserArrayOutput() PSQLUserArrayOutput {
	return i.ToPSQLUserArrayOutputWithContext(context.Background())
}

func (i PSQLUserArray) ToPSQLUserArrayOutputWithContext(ctx context.Context) PSQLUserArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PSQLUserArrayOutput)
}

// PSQLUserMapInput is an input type that accepts PSQLUserMap and PSQLUserMapOutput values.
// You can construct a concrete instance of `PSQLUserMapInput` via:
//
//	PSQLUserMap{ "key": PSQLUserArgs{...} }
type PSQLUserMapInput interface {
	pulumi.Input

	ToPSQLUserMapOutput() PSQLUserMapOutput
	ToPSQLUserMapOutputWithContext(context.Context) PSQLUserMapOutput
}

type PSQLUserMap map[string]PSQLUserInput

func (PSQLUserMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PSQLUser)(nil)).Elem()
}

func (i PSQLUserMap) ToPSQLUserMapOutput() PSQLUserMapOutput {
	return i.ToPSQLUserMapOutputWithContext(context.Background())
}

func (i PSQLUserMap) ToPSQLUserMapOutputWithContext(ctx context.Context) PSQLUserMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PSQLUserMapOutput)
}

type PSQLUserOutput struct{ *pulumi.OutputState }

func (PSQLUserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PSQLUser)(nil)).Elem()
}

func (o PSQLUserOutput) ToPSQLUserOutput() PSQLUserOutput {
	return o
}

func (o PSQLUserOutput) ToPSQLUserOutputWithContext(ctx context.Context) PSQLUserOutput {
	return o
}

// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
func (o PSQLUserOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *PSQLUser) pulumi.StringOutput { return v.ClusterId }).(pulumi.StringOutput)
}

// [bool] Describes whether this user is a system user or not. A system user cannot be updated or deleted.
func (o PSQLUserOutput) IsSystemUser() pulumi.BoolOutput {
	return o.ApplyT(func(v *PSQLUser) pulumi.BoolOutput { return v.IsSystemUser }).(pulumi.BoolOutput)
}

// [string] User password.
func (o PSQLUserOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *PSQLUser) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
func (o PSQLUserOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v *PSQLUser) pulumi.StringOutput { return v.Username }).(pulumi.StringOutput)
}

type PSQLUserArrayOutput struct{ *pulumi.OutputState }

func (PSQLUserArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PSQLUser)(nil)).Elem()
}

func (o PSQLUserArrayOutput) ToPSQLUserArrayOutput() PSQLUserArrayOutput {
	return o
}

func (o PSQLUserArrayOutput) ToPSQLUserArrayOutputWithContext(ctx context.Context) PSQLUserArrayOutput {
	return o
}

func (o PSQLUserArrayOutput) Index(i pulumi.IntInput) PSQLUserOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *PSQLUser {
		return vs[0].([]*PSQLUser)[vs[1].(int)]
	}).(PSQLUserOutput)
}

type PSQLUserMapOutput struct{ *pulumi.OutputState }

func (PSQLUserMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PSQLUser)(nil)).Elem()
}

func (o PSQLUserMapOutput) ToPSQLUserMapOutput() PSQLUserMapOutput {
	return o
}

func (o PSQLUserMapOutput) ToPSQLUserMapOutputWithContext(ctx context.Context) PSQLUserMapOutput {
	return o
}

func (o PSQLUserMapOutput) MapIndex(k pulumi.StringInput) PSQLUserOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *PSQLUser {
		return vs[0].(map[string]*PSQLUser)[vs[1].(string)]
	}).(PSQLUserOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PSQLUserInput)(nil)).Elem(), &PSQLUser{})
	pulumi.RegisterInputType(reflect.TypeOf((*PSQLUserArrayInput)(nil)).Elem(), PSQLUserArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PSQLUserMapInput)(nil)).Elem(), PSQLUserMap{})
	pulumi.RegisterOutputType(PSQLUserOutput{})
	pulumi.RegisterOutputType(PSQLUserArrayOutput{})
	pulumi.RegisterOutputType(PSQLUserMapOutput{})
}

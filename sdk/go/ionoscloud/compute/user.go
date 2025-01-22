// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages **Users** and list users and groups associated with that user.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi-random/sdk/go/random"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			group1, err := compute.NewGroup(ctx, "group1", &compute.GroupArgs{
//				Name:              pulumi.String("group1"),
//				CreateDatacenter:  pulumi.Bool(true),
//				CreateSnapshot:    pulumi.Bool(true),
//				ReserveIp:         pulumi.Bool(true),
//				AccessActivityLog: pulumi.Bool(false),
//				CreateK8sCluster:  pulumi.Bool(true),
//			})
//			if err != nil {
//				return err
//			}
//			group2, err := compute.NewGroup(ctx, "group2", &compute.GroupArgs{
//				Name:              pulumi.String("group2"),
//				CreateDatacenter:  pulumi.Bool(true),
//				CreateSnapshot:    pulumi.Bool(true),
//				ReserveIp:         pulumi.Bool(true),
//				AccessActivityLog: pulumi.Bool(false),
//				CreateK8sCluster:  pulumi.Bool(true),
//			})
//			if err != nil {
//				return err
//			}
//			group3, err := compute.NewGroup(ctx, "group3", &compute.GroupArgs{
//				Name:              pulumi.String("group3"),
//				CreateDatacenter:  pulumi.Bool(true),
//				CreateSnapshot:    pulumi.Bool(true),
//				ReserveIp:         pulumi.Bool(true),
//				AccessActivityLog: pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			userPassword, err := random.NewPassword(ctx, "user_password", &random.PasswordArgs{
//				Length:          16,
//				Special:         true,
//				OverrideSpecial: "!#$%&*()-_=+[]{}<>:?",
//			})
//			if err != nil {
//				return err
//			}
//			_, err = compute.NewUser(ctx, "example", &compute.UserArgs{
//				FirstName:     pulumi.String("example"),
//				LastName:      pulumi.String("example"),
//				Email:         pulumi.String("unique@email.com"),
//				Password:      userPassword.Result,
//				Administrator: pulumi.Bool(false),
//				ForceSecAuth:  pulumi.Bool(false),
//				Active:        pulumi.Bool(true),
//				GroupIds: pulumi.StringArray{
//					group1.ID(),
//					group2.ID(),
//					group3.ID(),
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
//
// ## Import
//
// Resource User can be imported using the `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:compute/user:User myuser user uuid
// ```
type User struct {
	pulumi.CustomResourceState

	// [Boolean] Indicates if the user is active
	Active pulumi.BoolPtrOutput `pulumi:"active"`
	// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
	Administrator pulumi.BoolPtrOutput `pulumi:"administrator"`
	// [string] An e-mail address for the user.
	Email pulumi.StringOutput `pulumi:"email"`
	// [string] A first name for the user.
	FirstName pulumi.StringOutput `pulumi:"firstName"`
	// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
	ForceSecAuth pulumi.BoolPtrOutput `pulumi:"forceSecAuth"`
	// [Set] The groups that this user will be a member of
	//
	// **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
	GroupIds pulumi.StringArrayOutput `pulumi:"groupIds"`
	// [string] A last name for the user.
	LastName pulumi.StringOutput `pulumi:"lastName"`
	// [string] A password for the user.
	Password pulumi.StringOutput `pulumi:"password"`
	// Canonical (IONOS Object Storage) id of the user for a given identity
	S3CanonicalUserId pulumi.StringOutput `pulumi:"s3CanonicalUserId"`
	// [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
	SecAuthActive pulumi.BoolOutput `pulumi:"secAuthActive"`
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOption) (*User, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Email == nil {
		return nil, errors.New("invalid value for required argument 'Email'")
	}
	if args.FirstName == nil {
		return nil, errors.New("invalid value for required argument 'FirstName'")
	}
	if args.LastName == nil {
		return nil, errors.New("invalid value for required argument 'LastName'")
	}
	if args.Password == nil {
		return nil, errors.New("invalid value for required argument 'Password'")
	}
	if args.Password != nil {
		args.Password = pulumi.ToSecret(args.Password).(pulumi.StringInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"password",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource User
	err := ctx.RegisterResource("ionoscloud:compute/user:User", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserState, opts ...pulumi.ResourceOption) (*User, error) {
	var resource User
	err := ctx.ReadResource("ionoscloud:compute/user:User", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering User resources.
type userState struct {
	// [Boolean] Indicates if the user is active
	Active *bool `pulumi:"active"`
	// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
	Administrator *bool `pulumi:"administrator"`
	// [string] An e-mail address for the user.
	Email *string `pulumi:"email"`
	// [string] A first name for the user.
	FirstName *string `pulumi:"firstName"`
	// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
	ForceSecAuth *bool `pulumi:"forceSecAuth"`
	// [Set] The groups that this user will be a member of
	//
	// **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
	GroupIds []string `pulumi:"groupIds"`
	// [string] A last name for the user.
	LastName *string `pulumi:"lastName"`
	// [string] A password for the user.
	Password *string `pulumi:"password"`
	// Canonical (IONOS Object Storage) id of the user for a given identity
	S3CanonicalUserId *string `pulumi:"s3CanonicalUserId"`
	// [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
	SecAuthActive *bool `pulumi:"secAuthActive"`
}

type UserState struct {
	// [Boolean] Indicates if the user is active
	Active pulumi.BoolPtrInput
	// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
	Administrator pulumi.BoolPtrInput
	// [string] An e-mail address for the user.
	Email pulumi.StringPtrInput
	// [string] A first name for the user.
	FirstName pulumi.StringPtrInput
	// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
	ForceSecAuth pulumi.BoolPtrInput
	// [Set] The groups that this user will be a member of
	//
	// **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
	GroupIds pulumi.StringArrayInput
	// [string] A last name for the user.
	LastName pulumi.StringPtrInput
	// [string] A password for the user.
	Password pulumi.StringPtrInput
	// Canonical (IONOS Object Storage) id of the user for a given identity
	S3CanonicalUserId pulumi.StringPtrInput
	// [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
	SecAuthActive pulumi.BoolPtrInput
}

func (UserState) ElementType() reflect.Type {
	return reflect.TypeOf((*userState)(nil)).Elem()
}

type userArgs struct {
	// [Boolean] Indicates if the user is active
	Active *bool `pulumi:"active"`
	// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
	Administrator *bool `pulumi:"administrator"`
	// [string] An e-mail address for the user.
	Email string `pulumi:"email"`
	// [string] A first name for the user.
	FirstName string `pulumi:"firstName"`
	// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
	ForceSecAuth *bool `pulumi:"forceSecAuth"`
	// [Set] The groups that this user will be a member of
	//
	// **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
	GroupIds []string `pulumi:"groupIds"`
	// [string] A last name for the user.
	LastName string `pulumi:"lastName"`
	// [string] A password for the user.
	Password string `pulumi:"password"`
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// [Boolean] Indicates if the user is active
	Active pulumi.BoolPtrInput
	// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
	Administrator pulumi.BoolPtrInput
	// [string] An e-mail address for the user.
	Email pulumi.StringInput
	// [string] A first name for the user.
	FirstName pulumi.StringInput
	// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
	ForceSecAuth pulumi.BoolPtrInput
	// [Set] The groups that this user will be a member of
	//
	// **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
	GroupIds pulumi.StringArrayInput
	// [string] A last name for the user.
	LastName pulumi.StringInput
	// [string] A password for the user.
	Password pulumi.StringInput
}

func (UserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userArgs)(nil)).Elem()
}

type UserInput interface {
	pulumi.Input

	ToUserOutput() UserOutput
	ToUserOutputWithContext(ctx context.Context) UserOutput
}

func (*User) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (i *User) ToUserOutput() UserOutput {
	return i.ToUserOutputWithContext(context.Background())
}

func (i *User) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserOutput)
}

// UserArrayInput is an input type that accepts UserArray and UserArrayOutput values.
// You can construct a concrete instance of `UserArrayInput` via:
//
//	UserArray{ UserArgs{...} }
type UserArrayInput interface {
	pulumi.Input

	ToUserArrayOutput() UserArrayOutput
	ToUserArrayOutputWithContext(context.Context) UserArrayOutput
}

type UserArray []UserInput

func (UserArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*User)(nil)).Elem()
}

func (i UserArray) ToUserArrayOutput() UserArrayOutput {
	return i.ToUserArrayOutputWithContext(context.Background())
}

func (i UserArray) ToUserArrayOutputWithContext(ctx context.Context) UserArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserArrayOutput)
}

// UserMapInput is an input type that accepts UserMap and UserMapOutput values.
// You can construct a concrete instance of `UserMapInput` via:
//
//	UserMap{ "key": UserArgs{...} }
type UserMapInput interface {
	pulumi.Input

	ToUserMapOutput() UserMapOutput
	ToUserMapOutputWithContext(context.Context) UserMapOutput
}

type UserMap map[string]UserInput

func (UserMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*User)(nil)).Elem()
}

func (i UserMap) ToUserMapOutput() UserMapOutput {
	return i.ToUserMapOutputWithContext(context.Background())
}

func (i UserMap) ToUserMapOutputWithContext(ctx context.Context) UserMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserMapOutput)
}

type UserOutput struct{ *pulumi.OutputState }

func (UserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (o UserOutput) ToUserOutput() UserOutput {
	return o
}

func (o UserOutput) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return o
}

// [Boolean] Indicates if the user is active
func (o UserOutput) Active() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *User) pulumi.BoolPtrOutput { return v.Active }).(pulumi.BoolPtrOutput)
}

// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
func (o UserOutput) Administrator() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *User) pulumi.BoolPtrOutput { return v.Administrator }).(pulumi.BoolPtrOutput)
}

// [string] An e-mail address for the user.
func (o UserOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.Email }).(pulumi.StringOutput)
}

// [string] A first name for the user.
func (o UserOutput) FirstName() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.FirstName }).(pulumi.StringOutput)
}

// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
func (o UserOutput) ForceSecAuth() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *User) pulumi.BoolPtrOutput { return v.ForceSecAuth }).(pulumi.BoolPtrOutput)
}

// [Set] The groups that this user will be a member of
//
// **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
func (o UserOutput) GroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *User) pulumi.StringArrayOutput { return v.GroupIds }).(pulumi.StringArrayOutput)
}

// [string] A last name for the user.
func (o UserOutput) LastName() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.LastName }).(pulumi.StringOutput)
}

// [string] A password for the user.
func (o UserOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

// Canonical (IONOS Object Storage) id of the user for a given identity
func (o UserOutput) S3CanonicalUserId() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.S3CanonicalUserId }).(pulumi.StringOutput)
}

// [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
func (o UserOutput) SecAuthActive() pulumi.BoolOutput {
	return o.ApplyT(func(v *User) pulumi.BoolOutput { return v.SecAuthActive }).(pulumi.BoolOutput)
}

type UserArrayOutput struct{ *pulumi.OutputState }

func (UserArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*User)(nil)).Elem()
}

func (o UserArrayOutput) ToUserArrayOutput() UserArrayOutput {
	return o
}

func (o UserArrayOutput) ToUserArrayOutputWithContext(ctx context.Context) UserArrayOutput {
	return o
}

func (o UserArrayOutput) Index(i pulumi.IntInput) UserOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *User {
		return vs[0].([]*User)[vs[1].(int)]
	}).(UserOutput)
}

type UserMapOutput struct{ *pulumi.OutputState }

func (UserMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*User)(nil)).Elem()
}

func (o UserMapOutput) ToUserMapOutput() UserMapOutput {
	return o
}

func (o UserMapOutput) ToUserMapOutputWithContext(ctx context.Context) UserMapOutput {
	return o
}

func (o UserMapOutput) MapIndex(k pulumi.StringInput) UserOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *User {
		return vs[0].(map[string]*User)[vs[1].(string)]
	}).(UserOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserInput)(nil)).Elem(), &User{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserArrayInput)(nil)).Elem(), UserArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserMapInput)(nil)).Elem(), UserMap{})
	pulumi.RegisterOutputType(UserOutput{})
	pulumi.RegisterOutputType(UserArrayOutput{})
	pulumi.RegisterOutputType(UserMapOutput{})
}

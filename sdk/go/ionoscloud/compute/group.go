// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages **Groups** and **Group Privileges** on IonosCloud.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi-random/sdk/v4/go/random"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			user1Password, err := random.NewRandomPassword(ctx, "user1Password", &random.RandomPasswordArgs{
//				Length:          pulumi.Int(16),
//				Special:         pulumi.Bool(true),
//				OverrideSpecial: pulumi.String("!#$%&*()-_=+[]{}<>:?"),
//			})
//			if err != nil {
//				return err
//			}
//			example1, err := compute.NewUser(ctx, "example1", &compute.UserArgs{
//				FirstName:     pulumi.String("user1"),
//				LastName:      pulumi.String("user1"),
//				Email:         pulumi.String("unique_email.com"),
//				Password:      user1Password.Result,
//				Administrator: pulumi.Bool(false),
//				ForceSecAuth:  pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			user2Password, err := random.NewRandomPassword(ctx, "user2Password", &random.RandomPasswordArgs{
//				Length:          pulumi.Int(16),
//				Special:         pulumi.Bool(true),
//				OverrideSpecial: pulumi.String("!#$%&*()-_=+[]{}<>:?"),
//			})
//			if err != nil {
//				return err
//			}
//			example2, err := compute.NewUser(ctx, "example2", &compute.UserArgs{
//				FirstName:     pulumi.String("user2"),
//				LastName:      pulumi.String("user2"),
//				Email:         pulumi.String("unique_email.com"),
//				Password:      user2Password.Result,
//				Administrator: pulumi.Bool(false),
//				ForceSecAuth:  pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = compute.NewGroup(ctx, "example", &compute.GroupArgs{
//				CreateDatacenter:            pulumi.Bool(true),
//				CreateSnapshot:              pulumi.Bool(true),
//				ReserveIp:                   pulumi.Bool(true),
//				AccessActivityLog:           pulumi.Bool(true),
//				CreatePcc:                   pulumi.Bool(true),
//				S3Privilege:                 pulumi.Bool(true),
//				CreateBackupUnit:            pulumi.Bool(true),
//				CreateInternetAccess:        pulumi.Bool(true),
//				CreateK8sCluster:            pulumi.Bool(true),
//				CreateFlowLog:               pulumi.Bool(true),
//				AccessAndManageMonitoring:   pulumi.Bool(true),
//				AccessAndManageCertificates: pulumi.Bool(true),
//				ManageDbaas:                 pulumi.Bool(true),
//				UserIds: pulumi.StringArray{
//					example1.ID(),
//					example2.ID(),
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
// Resource Group can be imported using the `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:compute/group:Group mygroup {group uuid}
// ```
//
// > :warning: **If you are upgrading to v6.2.0**: You have to modify you plan for user_ids to match the new structure, by renaming the field old field, **user_id**, to user_ids and put the old value into an array. This is not backwards compatible.
type Group struct {
	pulumi.CustomResourceState

	// [Boolean] The group will be allowed to access the activity log.
	AccessActivityLog pulumi.BoolPtrOutput `pulumi:"accessActivityLog"`
	// [Boolean]  The group will be allowed to access and manage certificates.
	AccessAndManageCertificates pulumi.BoolPtrOutput `pulumi:"accessAndManageCertificates"`
	// [Boolean]  The group will be allowed to access and manage monitoring.
	AccessAndManageMonitoring pulumi.BoolPtrOutput `pulumi:"accessAndManageMonitoring"`
	// [Boolean] The group will be allowed to create backup unit privilege.
	CreateBackupUnit pulumi.BoolPtrOutput `pulumi:"createBackupUnit"`
	// [Boolean] The group will be allowed to create virtual data centers.
	CreateDatacenter pulumi.BoolPtrOutput `pulumi:"createDatacenter"`
	// [Boolean]  The group will be allowed to create flow log.
	CreateFlowLog pulumi.BoolPtrOutput `pulumi:"createFlowLog"`
	// [Boolean] The group will be allowed to create internet access privilege.
	CreateInternetAccess pulumi.BoolPtrOutput `pulumi:"createInternetAccess"`
	// [Boolean]  The group will be allowed to create kubernetes cluster privilege.
	CreateK8sCluster pulumi.BoolPtrOutput `pulumi:"createK8sCluster"`
	// [Boolean] The group will be allowed to create Cross Connects privilege.
	CreatePcc pulumi.BoolPtrOutput `pulumi:"createPcc"`
	// [Boolean] The group will be allowed to create snapshots.
	CreateSnapshot pulumi.BoolPtrOutput `pulumi:"createSnapshot"`
	// [Boolean]  Privilege for a group to manage DBaaS related functionality.
	ManageDbaas pulumi.BoolPtrOutput `pulumi:"manageDbaas"`
	// [string] A name for the group.
	Name pulumi.StringOutput `pulumi:"name"`
	// [Boolean] The group will be allowed to reserve IP addresses.
	ReserveIp pulumi.BoolPtrOutput `pulumi:"reserveIp"`
	// [Boolean] The group will have S3 privilege.
	S3Privilege pulumi.BoolPtrOutput `pulumi:"s3Privilege"`
	// [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
	//
	// Deprecated: Please use userIds for adding users to the group, since userId will be removed in the future
	UserId pulumi.StringPtrOutput `pulumi:"userId"`
	// [list] A list of users to add to the group.
	UserIds pulumi.StringArrayOutput `pulumi:"userIds"`
	// List of users - See the User section
	//
	// **NOTE:** user_id/user_ids field cannot be used at the same time with groupIds field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
	Users GroupUserArrayOutput `pulumi:"users"`
}

// NewGroup registers a new resource with the given unique name, arguments, and options.
func NewGroup(ctx *pulumi.Context,
	name string, args *GroupArgs, opts ...pulumi.ResourceOption) (*Group, error) {
	if args == nil {
		args = &GroupArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Group
	err := ctx.RegisterResource("ionoscloud:compute/group:Group", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGroup gets an existing Group resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GroupState, opts ...pulumi.ResourceOption) (*Group, error) {
	var resource Group
	err := ctx.ReadResource("ionoscloud:compute/group:Group", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Group resources.
type groupState struct {
	// [Boolean] The group will be allowed to access the activity log.
	AccessActivityLog *bool `pulumi:"accessActivityLog"`
	// [Boolean]  The group will be allowed to access and manage certificates.
	AccessAndManageCertificates *bool `pulumi:"accessAndManageCertificates"`
	// [Boolean]  The group will be allowed to access and manage monitoring.
	AccessAndManageMonitoring *bool `pulumi:"accessAndManageMonitoring"`
	// [Boolean] The group will be allowed to create backup unit privilege.
	CreateBackupUnit *bool `pulumi:"createBackupUnit"`
	// [Boolean] The group will be allowed to create virtual data centers.
	CreateDatacenter *bool `pulumi:"createDatacenter"`
	// [Boolean]  The group will be allowed to create flow log.
	CreateFlowLog *bool `pulumi:"createFlowLog"`
	// [Boolean] The group will be allowed to create internet access privilege.
	CreateInternetAccess *bool `pulumi:"createInternetAccess"`
	// [Boolean]  The group will be allowed to create kubernetes cluster privilege.
	CreateK8sCluster *bool `pulumi:"createK8sCluster"`
	// [Boolean] The group will be allowed to create Cross Connects privilege.
	CreatePcc *bool `pulumi:"createPcc"`
	// [Boolean] The group will be allowed to create snapshots.
	CreateSnapshot *bool `pulumi:"createSnapshot"`
	// [Boolean]  Privilege for a group to manage DBaaS related functionality.
	ManageDbaas *bool `pulumi:"manageDbaas"`
	// [string] A name for the group.
	Name *string `pulumi:"name"`
	// [Boolean] The group will be allowed to reserve IP addresses.
	ReserveIp *bool `pulumi:"reserveIp"`
	// [Boolean] The group will have S3 privilege.
	S3Privilege *bool `pulumi:"s3Privilege"`
	// [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
	//
	// Deprecated: Please use userIds for adding users to the group, since userId will be removed in the future
	UserId *string `pulumi:"userId"`
	// [list] A list of users to add to the group.
	UserIds []string `pulumi:"userIds"`
	// List of users - See the User section
	//
	// **NOTE:** user_id/user_ids field cannot be used at the same time with groupIds field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
	Users []GroupUser `pulumi:"users"`
}

type GroupState struct {
	// [Boolean] The group will be allowed to access the activity log.
	AccessActivityLog pulumi.BoolPtrInput
	// [Boolean]  The group will be allowed to access and manage certificates.
	AccessAndManageCertificates pulumi.BoolPtrInput
	// [Boolean]  The group will be allowed to access and manage monitoring.
	AccessAndManageMonitoring pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create backup unit privilege.
	CreateBackupUnit pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create virtual data centers.
	CreateDatacenter pulumi.BoolPtrInput
	// [Boolean]  The group will be allowed to create flow log.
	CreateFlowLog pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create internet access privilege.
	CreateInternetAccess pulumi.BoolPtrInput
	// [Boolean]  The group will be allowed to create kubernetes cluster privilege.
	CreateK8sCluster pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create Cross Connects privilege.
	CreatePcc pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create snapshots.
	CreateSnapshot pulumi.BoolPtrInput
	// [Boolean]  Privilege for a group to manage DBaaS related functionality.
	ManageDbaas pulumi.BoolPtrInput
	// [string] A name for the group.
	Name pulumi.StringPtrInput
	// [Boolean] The group will be allowed to reserve IP addresses.
	ReserveIp pulumi.BoolPtrInput
	// [Boolean] The group will have S3 privilege.
	S3Privilege pulumi.BoolPtrInput
	// [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
	//
	// Deprecated: Please use userIds for adding users to the group, since userId will be removed in the future
	UserId pulumi.StringPtrInput
	// [list] A list of users to add to the group.
	UserIds pulumi.StringArrayInput
	// List of users - See the User section
	//
	// **NOTE:** user_id/user_ids field cannot be used at the same time with groupIds field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
	Users GroupUserArrayInput
}

func (GroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*groupState)(nil)).Elem()
}

type groupArgs struct {
	// [Boolean] The group will be allowed to access the activity log.
	AccessActivityLog *bool `pulumi:"accessActivityLog"`
	// [Boolean]  The group will be allowed to access and manage certificates.
	AccessAndManageCertificates *bool `pulumi:"accessAndManageCertificates"`
	// [Boolean]  The group will be allowed to access and manage monitoring.
	AccessAndManageMonitoring *bool `pulumi:"accessAndManageMonitoring"`
	// [Boolean] The group will be allowed to create backup unit privilege.
	CreateBackupUnit *bool `pulumi:"createBackupUnit"`
	// [Boolean] The group will be allowed to create virtual data centers.
	CreateDatacenter *bool `pulumi:"createDatacenter"`
	// [Boolean]  The group will be allowed to create flow log.
	CreateFlowLog *bool `pulumi:"createFlowLog"`
	// [Boolean] The group will be allowed to create internet access privilege.
	CreateInternetAccess *bool `pulumi:"createInternetAccess"`
	// [Boolean]  The group will be allowed to create kubernetes cluster privilege.
	CreateK8sCluster *bool `pulumi:"createK8sCluster"`
	// [Boolean] The group will be allowed to create Cross Connects privilege.
	CreatePcc *bool `pulumi:"createPcc"`
	// [Boolean] The group will be allowed to create snapshots.
	CreateSnapshot *bool `pulumi:"createSnapshot"`
	// [Boolean]  Privilege for a group to manage DBaaS related functionality.
	ManageDbaas *bool `pulumi:"manageDbaas"`
	// [string] A name for the group.
	Name *string `pulumi:"name"`
	// [Boolean] The group will be allowed to reserve IP addresses.
	ReserveIp *bool `pulumi:"reserveIp"`
	// [Boolean] The group will have S3 privilege.
	S3Privilege *bool `pulumi:"s3Privilege"`
	// [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
	//
	// Deprecated: Please use userIds for adding users to the group, since userId will be removed in the future
	UserId *string `pulumi:"userId"`
	// [list] A list of users to add to the group.
	UserIds []string `pulumi:"userIds"`
}

// The set of arguments for constructing a Group resource.
type GroupArgs struct {
	// [Boolean] The group will be allowed to access the activity log.
	AccessActivityLog pulumi.BoolPtrInput
	// [Boolean]  The group will be allowed to access and manage certificates.
	AccessAndManageCertificates pulumi.BoolPtrInput
	// [Boolean]  The group will be allowed to access and manage monitoring.
	AccessAndManageMonitoring pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create backup unit privilege.
	CreateBackupUnit pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create virtual data centers.
	CreateDatacenter pulumi.BoolPtrInput
	// [Boolean]  The group will be allowed to create flow log.
	CreateFlowLog pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create internet access privilege.
	CreateInternetAccess pulumi.BoolPtrInput
	// [Boolean]  The group will be allowed to create kubernetes cluster privilege.
	CreateK8sCluster pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create Cross Connects privilege.
	CreatePcc pulumi.BoolPtrInput
	// [Boolean] The group will be allowed to create snapshots.
	CreateSnapshot pulumi.BoolPtrInput
	// [Boolean]  Privilege for a group to manage DBaaS related functionality.
	ManageDbaas pulumi.BoolPtrInput
	// [string] A name for the group.
	Name pulumi.StringPtrInput
	// [Boolean] The group will be allowed to reserve IP addresses.
	ReserveIp pulumi.BoolPtrInput
	// [Boolean] The group will have S3 privilege.
	S3Privilege pulumi.BoolPtrInput
	// [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
	//
	// Deprecated: Please use userIds for adding users to the group, since userId will be removed in the future
	UserId pulumi.StringPtrInput
	// [list] A list of users to add to the group.
	UserIds pulumi.StringArrayInput
}

func (GroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*groupArgs)(nil)).Elem()
}

type GroupInput interface {
	pulumi.Input

	ToGroupOutput() GroupOutput
	ToGroupOutputWithContext(ctx context.Context) GroupOutput
}

func (*Group) ElementType() reflect.Type {
	return reflect.TypeOf((**Group)(nil)).Elem()
}

func (i *Group) ToGroupOutput() GroupOutput {
	return i.ToGroupOutputWithContext(context.Background())
}

func (i *Group) ToGroupOutputWithContext(ctx context.Context) GroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupOutput)
}

// GroupArrayInput is an input type that accepts GroupArray and GroupArrayOutput values.
// You can construct a concrete instance of `GroupArrayInput` via:
//
//	GroupArray{ GroupArgs{...} }
type GroupArrayInput interface {
	pulumi.Input

	ToGroupArrayOutput() GroupArrayOutput
	ToGroupArrayOutputWithContext(context.Context) GroupArrayOutput
}

type GroupArray []GroupInput

func (GroupArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Group)(nil)).Elem()
}

func (i GroupArray) ToGroupArrayOutput() GroupArrayOutput {
	return i.ToGroupArrayOutputWithContext(context.Background())
}

func (i GroupArray) ToGroupArrayOutputWithContext(ctx context.Context) GroupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupArrayOutput)
}

// GroupMapInput is an input type that accepts GroupMap and GroupMapOutput values.
// You can construct a concrete instance of `GroupMapInput` via:
//
//	GroupMap{ "key": GroupArgs{...} }
type GroupMapInput interface {
	pulumi.Input

	ToGroupMapOutput() GroupMapOutput
	ToGroupMapOutputWithContext(context.Context) GroupMapOutput
}

type GroupMap map[string]GroupInput

func (GroupMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Group)(nil)).Elem()
}

func (i GroupMap) ToGroupMapOutput() GroupMapOutput {
	return i.ToGroupMapOutputWithContext(context.Background())
}

func (i GroupMap) ToGroupMapOutputWithContext(ctx context.Context) GroupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMapOutput)
}

type GroupOutput struct{ *pulumi.OutputState }

func (GroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Group)(nil)).Elem()
}

func (o GroupOutput) ToGroupOutput() GroupOutput {
	return o
}

func (o GroupOutput) ToGroupOutputWithContext(ctx context.Context) GroupOutput {
	return o
}

// [Boolean] The group will be allowed to access the activity log.
func (o GroupOutput) AccessActivityLog() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.AccessActivityLog }).(pulumi.BoolPtrOutput)
}

// [Boolean]  The group will be allowed to access and manage certificates.
func (o GroupOutput) AccessAndManageCertificates() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.AccessAndManageCertificates }).(pulumi.BoolPtrOutput)
}

// [Boolean]  The group will be allowed to access and manage monitoring.
func (o GroupOutput) AccessAndManageMonitoring() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.AccessAndManageMonitoring }).(pulumi.BoolPtrOutput)
}

// [Boolean] The group will be allowed to create backup unit privilege.
func (o GroupOutput) CreateBackupUnit() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.CreateBackupUnit }).(pulumi.BoolPtrOutput)
}

// [Boolean] The group will be allowed to create virtual data centers.
func (o GroupOutput) CreateDatacenter() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.CreateDatacenter }).(pulumi.BoolPtrOutput)
}

// [Boolean]  The group will be allowed to create flow log.
func (o GroupOutput) CreateFlowLog() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.CreateFlowLog }).(pulumi.BoolPtrOutput)
}

// [Boolean] The group will be allowed to create internet access privilege.
func (o GroupOutput) CreateInternetAccess() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.CreateInternetAccess }).(pulumi.BoolPtrOutput)
}

// [Boolean]  The group will be allowed to create kubernetes cluster privilege.
func (o GroupOutput) CreateK8sCluster() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.CreateK8sCluster }).(pulumi.BoolPtrOutput)
}

// [Boolean] The group will be allowed to create Cross Connects privilege.
func (o GroupOutput) CreatePcc() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.CreatePcc }).(pulumi.BoolPtrOutput)
}

// [Boolean] The group will be allowed to create snapshots.
func (o GroupOutput) CreateSnapshot() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.CreateSnapshot }).(pulumi.BoolPtrOutput)
}

// [Boolean]  Privilege for a group to manage DBaaS related functionality.
func (o GroupOutput) ManageDbaas() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.ManageDbaas }).(pulumi.BoolPtrOutput)
}

// [string] A name for the group.
func (o GroupOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Group) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [Boolean] The group will be allowed to reserve IP addresses.
func (o GroupOutput) ReserveIp() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.ReserveIp }).(pulumi.BoolPtrOutput)
}

// [Boolean] The group will have S3 privilege.
func (o GroupOutput) S3Privilege() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.BoolPtrOutput { return v.S3Privilege }).(pulumi.BoolPtrOutput)
}

// [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
//
// Deprecated: Please use userIds for adding users to the group, since userId will be removed in the future
func (o GroupOutput) UserId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Group) pulumi.StringPtrOutput { return v.UserId }).(pulumi.StringPtrOutput)
}

// [list] A list of users to add to the group.
func (o GroupOutput) UserIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Group) pulumi.StringArrayOutput { return v.UserIds }).(pulumi.StringArrayOutput)
}

// List of users - See the User section
//
// **NOTE:** user_id/user_ids field cannot be used at the same time with groupIds field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
func (o GroupOutput) Users() GroupUserArrayOutput {
	return o.ApplyT(func(v *Group) GroupUserArrayOutput { return v.Users }).(GroupUserArrayOutput)
}

type GroupArrayOutput struct{ *pulumi.OutputState }

func (GroupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Group)(nil)).Elem()
}

func (o GroupArrayOutput) ToGroupArrayOutput() GroupArrayOutput {
	return o
}

func (o GroupArrayOutput) ToGroupArrayOutputWithContext(ctx context.Context) GroupArrayOutput {
	return o
}

func (o GroupArrayOutput) Index(i pulumi.IntInput) GroupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Group {
		return vs[0].([]*Group)[vs[1].(int)]
	}).(GroupOutput)
}

type GroupMapOutput struct{ *pulumi.OutputState }

func (GroupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Group)(nil)).Elem()
}

func (o GroupMapOutput) ToGroupMapOutput() GroupMapOutput {
	return o
}

func (o GroupMapOutput) ToGroupMapOutputWithContext(ctx context.Context) GroupMapOutput {
	return o
}

func (o GroupMapOutput) MapIndex(k pulumi.StringInput) GroupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Group {
		return vs[0].(map[string]*Group)[vs[1].(string)]
	}).(GroupOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GroupInput)(nil)).Elem(), &Group{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupArrayInput)(nil)).Elem(), GroupArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMapInput)(nil)).Elem(), GroupMap{})
	pulumi.RegisterOutputType(GroupOutput{})
	pulumi.RegisterOutputType(GroupArrayOutput{})
	pulumi.RegisterOutputType(GroupMapOutput{})
}

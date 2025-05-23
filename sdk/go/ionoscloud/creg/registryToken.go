// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package creg

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages an **Container Registry Token** on IonosCloud.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/creg"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			example, err := creg.NewRegistry(ctx, "example", &creg.RegistryArgs{
//				GarbageCollectionSchedule: &creg.RegistryGarbageCollectionScheduleArgs{
//					Days: pulumi.StringArray{
//						pulumi.String("Monday"),
//						pulumi.String("Tuesday"),
//					},
//					Time: pulumi.String("05:19:00+00:00"),
//				},
//				Location: pulumi.String("de/fra"),
//				Name:     pulumi.String("container-registry-example"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = creg.NewRegistryToken(ctx, "example", &creg.RegistryTokenArgs{
//				ExpiryDate: pulumi.String("2023-01-13 16:27:42Z"),
//				Name:       pulumi.String("container-registry-token-example"),
//				Scopes: creg.RegistryTokenScopeArray{
//					&creg.RegistryTokenScopeArgs{
//						Actions: pulumi.StringArray{
//							pulumi.String("push"),
//						},
//						Name: pulumi.String("Scope1"),
//						Type: pulumi.String("repository"),
//					},
//				},
//				Status:             pulumi.String("enabled"),
//				RegistryId:         example.ID(),
//				SavePasswordToFile: pulumi.String("pass.txt"),
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
// Resource Container Registry Token can be imported using the `container registry id` and `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:creg/registryToken:RegistryToken mycrtoken container_registry uuid/container_registry_token uuid
// ```
type RegistryToken struct {
	pulumi.CustomResourceState

	Credentials RegistryTokenCredentialArrayOutput `pulumi:"credentials"`
	ExpiryDate  pulumi.StringPtrOutput             `pulumi:"expiryDate"`
	// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
	// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
	Name       pulumi.StringOutput `pulumi:"name"`
	RegistryId pulumi.StringOutput `pulumi:"registryId"`
	// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
	//
	// > **⚠ WARNING** `savePasswordToFile` must be used with caution.
	// It will save the password(token) returned on create to a file. This is the only way to get the token.
	SavePasswordToFile pulumi.StringPtrOutput `pulumi:"savePasswordToFile"`
	// [map]
	Scopes RegistryTokenScopeArrayOutput `pulumi:"scopes"`
	// [string] Must have on of the values: `enabled`, `disabled`
	Status pulumi.StringOutput `pulumi:"status"`
}

// NewRegistryToken registers a new resource with the given unique name, arguments, and options.
func NewRegistryToken(ctx *pulumi.Context,
	name string, args *RegistryTokenArgs, opts ...pulumi.ResourceOption) (*RegistryToken, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RegistryId == nil {
		return nil, errors.New("invalid value for required argument 'RegistryId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RegistryToken
	err := ctx.RegisterResource("ionoscloud:creg/registryToken:RegistryToken", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegistryToken gets an existing RegistryToken resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegistryToken(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegistryTokenState, opts ...pulumi.ResourceOption) (*RegistryToken, error) {
	var resource RegistryToken
	err := ctx.ReadResource("ionoscloud:creg/registryToken:RegistryToken", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RegistryToken resources.
type registryTokenState struct {
	Credentials []RegistryTokenCredential `pulumi:"credentials"`
	ExpiryDate  *string                   `pulumi:"expiryDate"`
	// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
	// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
	Name       *string `pulumi:"name"`
	RegistryId *string `pulumi:"registryId"`
	// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
	//
	// > **⚠ WARNING** `savePasswordToFile` must be used with caution.
	// It will save the password(token) returned on create to a file. This is the only way to get the token.
	SavePasswordToFile *string `pulumi:"savePasswordToFile"`
	// [map]
	Scopes []RegistryTokenScope `pulumi:"scopes"`
	// [string] Must have on of the values: `enabled`, `disabled`
	Status *string `pulumi:"status"`
}

type RegistryTokenState struct {
	Credentials RegistryTokenCredentialArrayInput
	ExpiryDate  pulumi.StringPtrInput
	// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
	// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
	Name       pulumi.StringPtrInput
	RegistryId pulumi.StringPtrInput
	// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
	//
	// > **⚠ WARNING** `savePasswordToFile` must be used with caution.
	// It will save the password(token) returned on create to a file. This is the only way to get the token.
	SavePasswordToFile pulumi.StringPtrInput
	// [map]
	Scopes RegistryTokenScopeArrayInput
	// [string] Must have on of the values: `enabled`, `disabled`
	Status pulumi.StringPtrInput
}

func (RegistryTokenState) ElementType() reflect.Type {
	return reflect.TypeOf((*registryTokenState)(nil)).Elem()
}

type registryTokenArgs struct {
	ExpiryDate *string `pulumi:"expiryDate"`
	// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
	// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
	Name       *string `pulumi:"name"`
	RegistryId string  `pulumi:"registryId"`
	// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
	//
	// > **⚠ WARNING** `savePasswordToFile` must be used with caution.
	// It will save the password(token) returned on create to a file. This is the only way to get the token.
	SavePasswordToFile *string `pulumi:"savePasswordToFile"`
	// [map]
	Scopes []RegistryTokenScope `pulumi:"scopes"`
	// [string] Must have on of the values: `enabled`, `disabled`
	Status *string `pulumi:"status"`
}

// The set of arguments for constructing a RegistryToken resource.
type RegistryTokenArgs struct {
	ExpiryDate pulumi.StringPtrInput
	// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
	// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
	Name       pulumi.StringPtrInput
	RegistryId pulumi.StringInput
	// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
	//
	// > **⚠ WARNING** `savePasswordToFile` must be used with caution.
	// It will save the password(token) returned on create to a file. This is the only way to get the token.
	SavePasswordToFile pulumi.StringPtrInput
	// [map]
	Scopes RegistryTokenScopeArrayInput
	// [string] Must have on of the values: `enabled`, `disabled`
	Status pulumi.StringPtrInput
}

func (RegistryTokenArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*registryTokenArgs)(nil)).Elem()
}

type RegistryTokenInput interface {
	pulumi.Input

	ToRegistryTokenOutput() RegistryTokenOutput
	ToRegistryTokenOutputWithContext(ctx context.Context) RegistryTokenOutput
}

func (*RegistryToken) ElementType() reflect.Type {
	return reflect.TypeOf((**RegistryToken)(nil)).Elem()
}

func (i *RegistryToken) ToRegistryTokenOutput() RegistryTokenOutput {
	return i.ToRegistryTokenOutputWithContext(context.Background())
}

func (i *RegistryToken) ToRegistryTokenOutputWithContext(ctx context.Context) RegistryTokenOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegistryTokenOutput)
}

// RegistryTokenArrayInput is an input type that accepts RegistryTokenArray and RegistryTokenArrayOutput values.
// You can construct a concrete instance of `RegistryTokenArrayInput` via:
//
//	RegistryTokenArray{ RegistryTokenArgs{...} }
type RegistryTokenArrayInput interface {
	pulumi.Input

	ToRegistryTokenArrayOutput() RegistryTokenArrayOutput
	ToRegistryTokenArrayOutputWithContext(context.Context) RegistryTokenArrayOutput
}

type RegistryTokenArray []RegistryTokenInput

func (RegistryTokenArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RegistryToken)(nil)).Elem()
}

func (i RegistryTokenArray) ToRegistryTokenArrayOutput() RegistryTokenArrayOutput {
	return i.ToRegistryTokenArrayOutputWithContext(context.Background())
}

func (i RegistryTokenArray) ToRegistryTokenArrayOutputWithContext(ctx context.Context) RegistryTokenArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegistryTokenArrayOutput)
}

// RegistryTokenMapInput is an input type that accepts RegistryTokenMap and RegistryTokenMapOutput values.
// You can construct a concrete instance of `RegistryTokenMapInput` via:
//
//	RegistryTokenMap{ "key": RegistryTokenArgs{...} }
type RegistryTokenMapInput interface {
	pulumi.Input

	ToRegistryTokenMapOutput() RegistryTokenMapOutput
	ToRegistryTokenMapOutputWithContext(context.Context) RegistryTokenMapOutput
}

type RegistryTokenMap map[string]RegistryTokenInput

func (RegistryTokenMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RegistryToken)(nil)).Elem()
}

func (i RegistryTokenMap) ToRegistryTokenMapOutput() RegistryTokenMapOutput {
	return i.ToRegistryTokenMapOutputWithContext(context.Background())
}

func (i RegistryTokenMap) ToRegistryTokenMapOutputWithContext(ctx context.Context) RegistryTokenMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegistryTokenMapOutput)
}

type RegistryTokenOutput struct{ *pulumi.OutputState }

func (RegistryTokenOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RegistryToken)(nil)).Elem()
}

func (o RegistryTokenOutput) ToRegistryTokenOutput() RegistryTokenOutput {
	return o
}

func (o RegistryTokenOutput) ToRegistryTokenOutputWithContext(ctx context.Context) RegistryTokenOutput {
	return o
}

func (o RegistryTokenOutput) Credentials() RegistryTokenCredentialArrayOutput {
	return o.ApplyT(func(v *RegistryToken) RegistryTokenCredentialArrayOutput { return v.Credentials }).(RegistryTokenCredentialArrayOutput)
}

func (o RegistryTokenOutput) ExpiryDate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RegistryToken) pulumi.StringPtrOutput { return v.ExpiryDate }).(pulumi.StringPtrOutput)
}

// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
func (o RegistryTokenOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *RegistryToken) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o RegistryTokenOutput) RegistryId() pulumi.StringOutput {
	return o.ApplyT(func(v *RegistryToken) pulumi.StringOutput { return v.RegistryId }).(pulumi.StringOutput)
}

// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
//
// > **⚠ WARNING** `savePasswordToFile` must be used with caution.
// It will save the password(token) returned on create to a file. This is the only way to get the token.
func (o RegistryTokenOutput) SavePasswordToFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *RegistryToken) pulumi.StringPtrOutput { return v.SavePasswordToFile }).(pulumi.StringPtrOutput)
}

// [map]
func (o RegistryTokenOutput) Scopes() RegistryTokenScopeArrayOutput {
	return o.ApplyT(func(v *RegistryToken) RegistryTokenScopeArrayOutput { return v.Scopes }).(RegistryTokenScopeArrayOutput)
}

// [string] Must have on of the values: `enabled`, `disabled`
func (o RegistryTokenOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *RegistryToken) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

type RegistryTokenArrayOutput struct{ *pulumi.OutputState }

func (RegistryTokenArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RegistryToken)(nil)).Elem()
}

func (o RegistryTokenArrayOutput) ToRegistryTokenArrayOutput() RegistryTokenArrayOutput {
	return o
}

func (o RegistryTokenArrayOutput) ToRegistryTokenArrayOutputWithContext(ctx context.Context) RegistryTokenArrayOutput {
	return o
}

func (o RegistryTokenArrayOutput) Index(i pulumi.IntInput) RegistryTokenOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *RegistryToken {
		return vs[0].([]*RegistryToken)[vs[1].(int)]
	}).(RegistryTokenOutput)
}

type RegistryTokenMapOutput struct{ *pulumi.OutputState }

func (RegistryTokenMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RegistryToken)(nil)).Elem()
}

func (o RegistryTokenMapOutput) ToRegistryTokenMapOutput() RegistryTokenMapOutput {
	return o
}

func (o RegistryTokenMapOutput) ToRegistryTokenMapOutputWithContext(ctx context.Context) RegistryTokenMapOutput {
	return o
}

func (o RegistryTokenMapOutput) MapIndex(k pulumi.StringInput) RegistryTokenOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *RegistryToken {
		return vs[0].(map[string]*RegistryToken)[vs[1].(string)]
	}).(RegistryTokenOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RegistryTokenInput)(nil)).Elem(), &RegistryToken{})
	pulumi.RegisterInputType(reflect.TypeOf((*RegistryTokenArrayInput)(nil)).Elem(), RegistryTokenArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*RegistryTokenMapInput)(nil)).Elem(), RegistryTokenMap{})
	pulumi.RegisterOutputType(RegistryTokenOutput{})
	pulumi.RegisterOutputType(RegistryTokenArrayOutput{})
	pulumi.RegisterOutputType(RegistryTokenMapOutput{})
}

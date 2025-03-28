// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package objectstorage

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages Website Configuration for Buckets on IonosCloud.
//
// ## Import
//
// IONOS Object Storage Bucket website configuration can be imported using the `bucket` name.
//
// ```sh
// $ pulumi import ionoscloud:objectstorage/websiteConfiguration:WebsiteConfiguration example example
// ```
type WebsiteConfiguration struct {
	pulumi.CustomResourceState

	// [string] The name of the bucket where the object will be stored.
	Bucket pulumi.StringOutput `pulumi:"bucket"`
	// The object key name to use when a 4XX class error occurs. Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests
	ErrorDocument WebsiteConfigurationErrorDocumentPtrOutput `pulumi:"errorDocument"`
	// Container for the Suffix element.
	IndexDocument WebsiteConfigurationIndexDocumentPtrOutput `pulumi:"indexDocument"`
	// Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
	RedirectAllRequestsTo WebsiteConfigurationRedirectAllRequestsToPtrOutput `pulumi:"redirectAllRequestsTo"`
	// A container for describing a condition that must be met for the specified redirect to apply.
	RoutingRules WebsiteConfigurationRoutingRuleArrayOutput `pulumi:"routingRules"`
}

// NewWebsiteConfiguration registers a new resource with the given unique name, arguments, and options.
func NewWebsiteConfiguration(ctx *pulumi.Context,
	name string, args *WebsiteConfigurationArgs, opts ...pulumi.ResourceOption) (*WebsiteConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Bucket == nil {
		return nil, errors.New("invalid value for required argument 'Bucket'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource WebsiteConfiguration
	err := ctx.RegisterResource("ionoscloud:objectstorage/websiteConfiguration:WebsiteConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWebsiteConfiguration gets an existing WebsiteConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWebsiteConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WebsiteConfigurationState, opts ...pulumi.ResourceOption) (*WebsiteConfiguration, error) {
	var resource WebsiteConfiguration
	err := ctx.ReadResource("ionoscloud:objectstorage/websiteConfiguration:WebsiteConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WebsiteConfiguration resources.
type websiteConfigurationState struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket *string `pulumi:"bucket"`
	// The object key name to use when a 4XX class error occurs. Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests
	ErrorDocument *WebsiteConfigurationErrorDocument `pulumi:"errorDocument"`
	// Container for the Suffix element.
	IndexDocument *WebsiteConfigurationIndexDocument `pulumi:"indexDocument"`
	// Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
	RedirectAllRequestsTo *WebsiteConfigurationRedirectAllRequestsTo `pulumi:"redirectAllRequestsTo"`
	// A container for describing a condition that must be met for the specified redirect to apply.
	RoutingRules []WebsiteConfigurationRoutingRule `pulumi:"routingRules"`
}

type WebsiteConfigurationState struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket pulumi.StringPtrInput
	// The object key name to use when a 4XX class error occurs. Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests
	ErrorDocument WebsiteConfigurationErrorDocumentPtrInput
	// Container for the Suffix element.
	IndexDocument WebsiteConfigurationIndexDocumentPtrInput
	// Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
	RedirectAllRequestsTo WebsiteConfigurationRedirectAllRequestsToPtrInput
	// A container for describing a condition that must be met for the specified redirect to apply.
	RoutingRules WebsiteConfigurationRoutingRuleArrayInput
}

func (WebsiteConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*websiteConfigurationState)(nil)).Elem()
}

type websiteConfigurationArgs struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket string `pulumi:"bucket"`
	// The object key name to use when a 4XX class error occurs. Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests
	ErrorDocument *WebsiteConfigurationErrorDocument `pulumi:"errorDocument"`
	// Container for the Suffix element.
	IndexDocument *WebsiteConfigurationIndexDocument `pulumi:"indexDocument"`
	// Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
	RedirectAllRequestsTo *WebsiteConfigurationRedirectAllRequestsTo `pulumi:"redirectAllRequestsTo"`
	// A container for describing a condition that must be met for the specified redirect to apply.
	RoutingRules []WebsiteConfigurationRoutingRule `pulumi:"routingRules"`
}

// The set of arguments for constructing a WebsiteConfiguration resource.
type WebsiteConfigurationArgs struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket pulumi.StringInput
	// The object key name to use when a 4XX class error occurs. Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests
	ErrorDocument WebsiteConfigurationErrorDocumentPtrInput
	// Container for the Suffix element.
	IndexDocument WebsiteConfigurationIndexDocumentPtrInput
	// Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
	RedirectAllRequestsTo WebsiteConfigurationRedirectAllRequestsToPtrInput
	// A container for describing a condition that must be met for the specified redirect to apply.
	RoutingRules WebsiteConfigurationRoutingRuleArrayInput
}

func (WebsiteConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*websiteConfigurationArgs)(nil)).Elem()
}

type WebsiteConfigurationInput interface {
	pulumi.Input

	ToWebsiteConfigurationOutput() WebsiteConfigurationOutput
	ToWebsiteConfigurationOutputWithContext(ctx context.Context) WebsiteConfigurationOutput
}

func (*WebsiteConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((**WebsiteConfiguration)(nil)).Elem()
}

func (i *WebsiteConfiguration) ToWebsiteConfigurationOutput() WebsiteConfigurationOutput {
	return i.ToWebsiteConfigurationOutputWithContext(context.Background())
}

func (i *WebsiteConfiguration) ToWebsiteConfigurationOutputWithContext(ctx context.Context) WebsiteConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebsiteConfigurationOutput)
}

// WebsiteConfigurationArrayInput is an input type that accepts WebsiteConfigurationArray and WebsiteConfigurationArrayOutput values.
// You can construct a concrete instance of `WebsiteConfigurationArrayInput` via:
//
//	WebsiteConfigurationArray{ WebsiteConfigurationArgs{...} }
type WebsiteConfigurationArrayInput interface {
	pulumi.Input

	ToWebsiteConfigurationArrayOutput() WebsiteConfigurationArrayOutput
	ToWebsiteConfigurationArrayOutputWithContext(context.Context) WebsiteConfigurationArrayOutput
}

type WebsiteConfigurationArray []WebsiteConfigurationInput

func (WebsiteConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WebsiteConfiguration)(nil)).Elem()
}

func (i WebsiteConfigurationArray) ToWebsiteConfigurationArrayOutput() WebsiteConfigurationArrayOutput {
	return i.ToWebsiteConfigurationArrayOutputWithContext(context.Background())
}

func (i WebsiteConfigurationArray) ToWebsiteConfigurationArrayOutputWithContext(ctx context.Context) WebsiteConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebsiteConfigurationArrayOutput)
}

// WebsiteConfigurationMapInput is an input type that accepts WebsiteConfigurationMap and WebsiteConfigurationMapOutput values.
// You can construct a concrete instance of `WebsiteConfigurationMapInput` via:
//
//	WebsiteConfigurationMap{ "key": WebsiteConfigurationArgs{...} }
type WebsiteConfigurationMapInput interface {
	pulumi.Input

	ToWebsiteConfigurationMapOutput() WebsiteConfigurationMapOutput
	ToWebsiteConfigurationMapOutputWithContext(context.Context) WebsiteConfigurationMapOutput
}

type WebsiteConfigurationMap map[string]WebsiteConfigurationInput

func (WebsiteConfigurationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WebsiteConfiguration)(nil)).Elem()
}

func (i WebsiteConfigurationMap) ToWebsiteConfigurationMapOutput() WebsiteConfigurationMapOutput {
	return i.ToWebsiteConfigurationMapOutputWithContext(context.Background())
}

func (i WebsiteConfigurationMap) ToWebsiteConfigurationMapOutputWithContext(ctx context.Context) WebsiteConfigurationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebsiteConfigurationMapOutput)
}

type WebsiteConfigurationOutput struct{ *pulumi.OutputState }

func (WebsiteConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WebsiteConfiguration)(nil)).Elem()
}

func (o WebsiteConfigurationOutput) ToWebsiteConfigurationOutput() WebsiteConfigurationOutput {
	return o
}

func (o WebsiteConfigurationOutput) ToWebsiteConfigurationOutputWithContext(ctx context.Context) WebsiteConfigurationOutput {
	return o
}

// [string] The name of the bucket where the object will be stored.
func (o WebsiteConfigurationOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v *WebsiteConfiguration) pulumi.StringOutput { return v.Bucket }).(pulumi.StringOutput)
}

// The object key name to use when a 4XX class error occurs. Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests
func (o WebsiteConfigurationOutput) ErrorDocument() WebsiteConfigurationErrorDocumentPtrOutput {
	return o.ApplyT(func(v *WebsiteConfiguration) WebsiteConfigurationErrorDocumentPtrOutput { return v.ErrorDocument }).(WebsiteConfigurationErrorDocumentPtrOutput)
}

// Container for the Suffix element.
func (o WebsiteConfigurationOutput) IndexDocument() WebsiteConfigurationIndexDocumentPtrOutput {
	return o.ApplyT(func(v *WebsiteConfiguration) WebsiteConfigurationIndexDocumentPtrOutput { return v.IndexDocument }).(WebsiteConfigurationIndexDocumentPtrOutput)
}

// Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can can specify a different error code to return.
func (o WebsiteConfigurationOutput) RedirectAllRequestsTo() WebsiteConfigurationRedirectAllRequestsToPtrOutput {
	return o.ApplyT(func(v *WebsiteConfiguration) WebsiteConfigurationRedirectAllRequestsToPtrOutput {
		return v.RedirectAllRequestsTo
	}).(WebsiteConfigurationRedirectAllRequestsToPtrOutput)
}

// A container for describing a condition that must be met for the specified redirect to apply.
func (o WebsiteConfigurationOutput) RoutingRules() WebsiteConfigurationRoutingRuleArrayOutput {
	return o.ApplyT(func(v *WebsiteConfiguration) WebsiteConfigurationRoutingRuleArrayOutput { return v.RoutingRules }).(WebsiteConfigurationRoutingRuleArrayOutput)
}

type WebsiteConfigurationArrayOutput struct{ *pulumi.OutputState }

func (WebsiteConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WebsiteConfiguration)(nil)).Elem()
}

func (o WebsiteConfigurationArrayOutput) ToWebsiteConfigurationArrayOutput() WebsiteConfigurationArrayOutput {
	return o
}

func (o WebsiteConfigurationArrayOutput) ToWebsiteConfigurationArrayOutputWithContext(ctx context.Context) WebsiteConfigurationArrayOutput {
	return o
}

func (o WebsiteConfigurationArrayOutput) Index(i pulumi.IntInput) WebsiteConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *WebsiteConfiguration {
		return vs[0].([]*WebsiteConfiguration)[vs[1].(int)]
	}).(WebsiteConfigurationOutput)
}

type WebsiteConfigurationMapOutput struct{ *pulumi.OutputState }

func (WebsiteConfigurationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WebsiteConfiguration)(nil)).Elem()
}

func (o WebsiteConfigurationMapOutput) ToWebsiteConfigurationMapOutput() WebsiteConfigurationMapOutput {
	return o
}

func (o WebsiteConfigurationMapOutput) ToWebsiteConfigurationMapOutputWithContext(ctx context.Context) WebsiteConfigurationMapOutput {
	return o
}

func (o WebsiteConfigurationMapOutput) MapIndex(k pulumi.StringInput) WebsiteConfigurationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *WebsiteConfiguration {
		return vs[0].(map[string]*WebsiteConfiguration)[vs[1].(string)]
	}).(WebsiteConfigurationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WebsiteConfigurationInput)(nil)).Elem(), &WebsiteConfiguration{})
	pulumi.RegisterInputType(reflect.TypeOf((*WebsiteConfigurationArrayInput)(nil)).Elem(), WebsiteConfigurationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WebsiteConfigurationMapInput)(nil)).Elem(), WebsiteConfigurationMap{})
	pulumi.RegisterOutputType(WebsiteConfigurationOutput{})
	pulumi.RegisterOutputType(WebsiteConfigurationArrayOutput{})
	pulumi.RegisterOutputType(WebsiteConfigurationMapOutput{})
}

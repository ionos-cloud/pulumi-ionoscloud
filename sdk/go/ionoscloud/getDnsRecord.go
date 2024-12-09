// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **DNS Record** can be used to search for and return an existing DNS Record.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search and make sure that your resources have unique names.
//
// > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_record** data source. Please ensure you are using tokens as other methods will not be valid.
//
// ## Example Usage
func GetDnsRecord(ctx *pulumi.Context, args *GetDnsRecordArgs, opts ...pulumi.InvokeOption) (*GetDnsRecordResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetDnsRecordResult
	err := ctx.Invoke("ionoscloud:index/getDnsRecord:getDnsRecord", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDnsRecord.
type GetDnsRecordArgs struct {
	// [string] The ID of the DNS Record you want to search for.
	Id *string `pulumi:"id"`
	// [string] The name of the DNS Record you want to search for.
	Name *string `pulumi:"name"`
	// [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
	//
	// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
	PartialMatch *bool `pulumi:"partialMatch"`
	// [string] The ID of the DNS Zone in which the DNS Record can be found.
	ZoneId string `pulumi:"zoneId"`
}

// A collection of values returned by getDnsRecord.
type GetDnsRecordResult struct {
	// The content of the DNS Record.
	Content string `pulumi:"content"`
	// Indicates if the DNS Record is active or not.
	Enabled bool   `pulumi:"enabled"`
	Fqdn    string `pulumi:"fqdn"`
	// The UUID of the DNS Record.
	Id *string `pulumi:"id"`
	// The name of the DNS Record.
	Name         *string `pulumi:"name"`
	PartialMatch *bool   `pulumi:"partialMatch"`
	// The priority for the DNS Record.
	Priority int `pulumi:"priority"`
	// The time to live of the DNS Record.
	Ttl int `pulumi:"ttl"`
	// The type of the DNS Record.
	Type   string `pulumi:"type"`
	ZoneId string `pulumi:"zoneId"`
}

func GetDnsRecordOutput(ctx *pulumi.Context, args GetDnsRecordOutputArgs, opts ...pulumi.InvokeOption) GetDnsRecordResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetDnsRecordResultOutput, error) {
			args := v.(GetDnsRecordArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetDnsRecordResult
			secret, err := ctx.InvokePackageRaw("ionoscloud:index/getDnsRecord:getDnsRecord", args, &rv, "", opts...)
			if err != nil {
				return GetDnsRecordResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetDnsRecordResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetDnsRecordResultOutput), nil
			}
			return output, nil
		}).(GetDnsRecordResultOutput)
}

// A collection of arguments for invoking getDnsRecord.
type GetDnsRecordOutputArgs struct {
	// [string] The ID of the DNS Record you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// [string] The name of the DNS Record you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
	//
	// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
	PartialMatch pulumi.BoolPtrInput `pulumi:"partialMatch"`
	// [string] The ID of the DNS Zone in which the DNS Record can be found.
	ZoneId pulumi.StringInput `pulumi:"zoneId"`
}

func (GetDnsRecordOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDnsRecordArgs)(nil)).Elem()
}

// A collection of values returned by getDnsRecord.
type GetDnsRecordResultOutput struct{ *pulumi.OutputState }

func (GetDnsRecordResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDnsRecordResult)(nil)).Elem()
}

func (o GetDnsRecordResultOutput) ToGetDnsRecordResultOutput() GetDnsRecordResultOutput {
	return o
}

func (o GetDnsRecordResultOutput) ToGetDnsRecordResultOutputWithContext(ctx context.Context) GetDnsRecordResultOutput {
	return o
}

// The content of the DNS Record.
func (o GetDnsRecordResultOutput) Content() pulumi.StringOutput {
	return o.ApplyT(func(v GetDnsRecordResult) string { return v.Content }).(pulumi.StringOutput)
}

// Indicates if the DNS Record is active or not.
func (o GetDnsRecordResultOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v GetDnsRecordResult) bool { return v.Enabled }).(pulumi.BoolOutput)
}

func (o GetDnsRecordResultOutput) Fqdn() pulumi.StringOutput {
	return o.ApplyT(func(v GetDnsRecordResult) string { return v.Fqdn }).(pulumi.StringOutput)
}

// The UUID of the DNS Record.
func (o GetDnsRecordResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetDnsRecordResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The name of the DNS Record.
func (o GetDnsRecordResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetDnsRecordResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o GetDnsRecordResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v GetDnsRecordResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// The priority for the DNS Record.
func (o GetDnsRecordResultOutput) Priority() pulumi.IntOutput {
	return o.ApplyT(func(v GetDnsRecordResult) int { return v.Priority }).(pulumi.IntOutput)
}

// The time to live of the DNS Record.
func (o GetDnsRecordResultOutput) Ttl() pulumi.IntOutput {
	return o.ApplyT(func(v GetDnsRecordResult) int { return v.Ttl }).(pulumi.IntOutput)
}

// The type of the DNS Record.
func (o GetDnsRecordResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v GetDnsRecordResult) string { return v.Type }).(pulumi.StringOutput)
}

func (o GetDnsRecordResultOutput) ZoneId() pulumi.StringOutput {
	return o.ApplyT(func(v GetDnsRecordResult) string { return v.ZoneId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetDnsRecordResultOutput{})
}

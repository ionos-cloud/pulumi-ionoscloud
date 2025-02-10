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

// Manages **IONOS Object Storage Objects** on IonosCloud.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/objectstorage"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			exampleBucket, err := objectstorage.NewBucket(ctx, "exampleBucket", &objectstorage.BucketArgs{
//				ObjectLockEnabled: pulumi.Bool(true),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = objectstorage.NewObject(ctx, "exampleObject", &objectstorage.ObjectArgs{
//				Bucket:                    exampleBucket.Name,
//				Key:                       pulumi.String("object"),
//				Content:                   pulumi.String("body"),
//				ContentType:               pulumi.String("text/plain"),
//				CacheControl:              pulumi.String("no-cache"),
//				ContentDisposition:        pulumi.String("attachment"),
//				ContentEncoding:           pulumi.String("identity"),
//				ContentLanguage:           pulumi.String("en-GB"),
//				Expires:                   pulumi.String("2024-10-07T12:34:56Z"),
//				WebsiteRedirect:           pulumi.String("https://www.ionos.com"),
//				ServerSideEncryption:      pulumi.String("AES256"),
//				ObjectLockMode:            pulumi.String("GOVERNANCE"),
//				ObjectLockRetainUntilDate: pulumi.String("2024-10-07T12:34:56Z"),
//				ObjectLockLegalHold:       pulumi.String("ON"),
//				Tags: pulumi.StringMap{
//					"tk": pulumi.String("tv"),
//				},
//				Metadata: pulumi.StringMap{
//					"mk": pulumi.String("mv"),
//				},
//				ForceDestroy: pulumi.Bool(true),
//			})
//			if err != nil {
//				return err
//			}
//			// Upload from file
//			_, err = objectstorage.NewObject(ctx, "exampleObjectstorage/objectObject", &objectstorage.ObjectArgs{
//				Bucket: exampleBucket.Name,
//				Key:    pulumi.String("file-object"),
//				Source: pulumi.String("path/to/file"),
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
// Resource Object can be imported using the `bucket name` and `object key`
//
// ```sh
// $ pulumi import ionoscloud:objectstorage/object:Object example example/object
// ```
type Object struct {
	pulumi.CustomResourceState

	// [string] The name of the bucket where the object will be stored. Must be between 3 and 63 characters.
	Bucket pulumi.StringOutput `pulumi:"bucket"`
	// [string] Specifies caching behavior along the request/reply chain.
	CacheControl pulumi.StringPtrOutput `pulumi:"cacheControl"`
	// [string] Inline content of the object.
	Content pulumi.StringPtrOutput `pulumi:"content"`
	// [string] Specifies presentational information for the object.
	ContentDisposition pulumi.StringPtrOutput `pulumi:"contentDisposition"`
	// [string] Specifies what content encodings have been applied to the object.
	ContentEncoding pulumi.StringPtrOutput `pulumi:"contentEncoding"`
	// [string] The natural language or languages of the intended audience for the object.
	ContentLanguage pulumi.StringPtrOutput `pulumi:"contentLanguage"`
	// [string] A standard MIME type describing the format of the contents.
	ContentType pulumi.StringOutput `pulumi:"contentType"`
	// [string] An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.
	Etag pulumi.StringOutput `pulumi:"etag"`
	// [string] The date and time at which the object is no longer cacheable.
	Expires pulumi.StringPtrOutput `pulumi:"expires"`
	// [bool] If true, the object will be destroyed if versioning is enabled then all versions will be destroyed. Default is `false`.
	ForceDestroy pulumi.BoolOutput `pulumi:"forceDestroy"`
	// [string] The key of the object. Must be at least 1 character long.
	Key pulumi.StringOutput `pulumi:"key"`
	// [map] A map of metadata to store with the object in IONOS Object Storage. Metadata keys must be lowercase alphanumeric characters.
	Metadata pulumi.StringMapOutput `pulumi:"metadata"`
	// [string]The concatenation of the authentication device's serial number, a space, and the value displayed on your authentication device.
	Mfa pulumi.StringPtrOutput `pulumi:"mfa"`
	// [string] Indicates whether a legal hold is in effect for the object. Valid values are `ON` and `OFF`.
	ObjectLockLegalHold pulumi.StringPtrOutput `pulumi:"objectLockLegalHold"`
	// [string] The object lock mode that you want to apply to the object. Valid values are `GOVERNANCE` and `COMPLIANCE`.
	ObjectLockMode pulumi.StringPtrOutput `pulumi:"objectLockMode"`
	// [string] The date and time when the object lock retention expires.Must be in RFC3999 format
	ObjectLockRetainUntilDate pulumi.StringPtrOutput `pulumi:"objectLockRetainUntilDate"`
	// [string] Confirms that the requester knows that they will be charged for the request.
	RequestPayer pulumi.StringPtrOutput `pulumi:"requestPayer"`
	// [string] The server-side encryption algorithm used when storing this object in IONOS Object Storage. Valid value is AES256.
	ServerSideEncryption pulumi.StringOutput `pulumi:"serverSideEncryption"`
	// [string] Specifies the IONOS Object Storage Encryption Context for object encryption.
	ServerSideEncryptionContext pulumi.StringPtrOutput `pulumi:"serverSideEncryptionContext"`
	// [string] Specifies the algorithm to use for encrypting the object. Valid value is AES256.
	ServerSideEncryptionCustomerAlgorithm pulumi.StringPtrOutput `pulumi:"serverSideEncryptionCustomerAlgorithm"`
	// [string] Specifies the 256-bit, base64-encoded encryption key to use to encrypt and decrypt your data.
	ServerSideEncryptionCustomerKey pulumi.StringPtrOutput `pulumi:"serverSideEncryptionCustomerKey"`
	// [string] Specifies the 128-bit MD5 digest of the encryption key.
	ServerSideEncryptionCustomerKeyMd5 pulumi.StringPtrOutput `pulumi:"serverSideEncryptionCustomerKeyMd5"`
	// [string] The path to the file to upload.
	Source pulumi.StringPtrOutput `pulumi:"source"`
	// [string] The storage class of the object. Valid value is STANDARD. Default is STANDARD.
	StorageClass pulumi.StringOutput `pulumi:"storageClass"`
	// [map] The tag-set for the object.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// [string] The version of the object.
	VersionId pulumi.StringOutput `pulumi:"versionId"`
	// [string] Redirects requests for this object to another object in the same bucket or to an external URL.
	WebsiteRedirect pulumi.StringPtrOutput `pulumi:"websiteRedirect"`
}

// NewObject registers a new resource with the given unique name, arguments, and options.
func NewObject(ctx *pulumi.Context,
	name string, args *ObjectArgs, opts ...pulumi.ResourceOption) (*Object, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Bucket == nil {
		return nil, errors.New("invalid value for required argument 'Bucket'")
	}
	if args.Key == nil {
		return nil, errors.New("invalid value for required argument 'Key'")
	}
	if args.ServerSideEncryptionContext != nil {
		args.ServerSideEncryptionContext = pulumi.ToSecret(args.ServerSideEncryptionContext).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"serverSideEncryptionContext",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Object
	err := ctx.RegisterResource("ionoscloud:objectstorage/object:Object", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetObject gets an existing Object resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetObject(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ObjectState, opts ...pulumi.ResourceOption) (*Object, error) {
	var resource Object
	err := ctx.ReadResource("ionoscloud:objectstorage/object:Object", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Object resources.
type objectState struct {
	// [string] The name of the bucket where the object will be stored. Must be between 3 and 63 characters.
	Bucket *string `pulumi:"bucket"`
	// [string] Specifies caching behavior along the request/reply chain.
	CacheControl *string `pulumi:"cacheControl"`
	// [string] Inline content of the object.
	Content *string `pulumi:"content"`
	// [string] Specifies presentational information for the object.
	ContentDisposition *string `pulumi:"contentDisposition"`
	// [string] Specifies what content encodings have been applied to the object.
	ContentEncoding *string `pulumi:"contentEncoding"`
	// [string] The natural language or languages of the intended audience for the object.
	ContentLanguage *string `pulumi:"contentLanguage"`
	// [string] A standard MIME type describing the format of the contents.
	ContentType *string `pulumi:"contentType"`
	// [string] An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.
	Etag *string `pulumi:"etag"`
	// [string] The date and time at which the object is no longer cacheable.
	Expires *string `pulumi:"expires"`
	// [bool] If true, the object will be destroyed if versioning is enabled then all versions will be destroyed. Default is `false`.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// [string] The key of the object. Must be at least 1 character long.
	Key *string `pulumi:"key"`
	// [map] A map of metadata to store with the object in IONOS Object Storage. Metadata keys must be lowercase alphanumeric characters.
	Metadata map[string]string `pulumi:"metadata"`
	// [string]The concatenation of the authentication device's serial number, a space, and the value displayed on your authentication device.
	Mfa *string `pulumi:"mfa"`
	// [string] Indicates whether a legal hold is in effect for the object. Valid values are `ON` and `OFF`.
	ObjectLockLegalHold *string `pulumi:"objectLockLegalHold"`
	// [string] The object lock mode that you want to apply to the object. Valid values are `GOVERNANCE` and `COMPLIANCE`.
	ObjectLockMode *string `pulumi:"objectLockMode"`
	// [string] The date and time when the object lock retention expires.Must be in RFC3999 format
	ObjectLockRetainUntilDate *string `pulumi:"objectLockRetainUntilDate"`
	// [string] Confirms that the requester knows that they will be charged for the request.
	RequestPayer *string `pulumi:"requestPayer"`
	// [string] The server-side encryption algorithm used when storing this object in IONOS Object Storage. Valid value is AES256.
	ServerSideEncryption *string `pulumi:"serverSideEncryption"`
	// [string] Specifies the IONOS Object Storage Encryption Context for object encryption.
	ServerSideEncryptionContext *string `pulumi:"serverSideEncryptionContext"`
	// [string] Specifies the algorithm to use for encrypting the object. Valid value is AES256.
	ServerSideEncryptionCustomerAlgorithm *string `pulumi:"serverSideEncryptionCustomerAlgorithm"`
	// [string] Specifies the 256-bit, base64-encoded encryption key to use to encrypt and decrypt your data.
	ServerSideEncryptionCustomerKey *string `pulumi:"serverSideEncryptionCustomerKey"`
	// [string] Specifies the 128-bit MD5 digest of the encryption key.
	ServerSideEncryptionCustomerKeyMd5 *string `pulumi:"serverSideEncryptionCustomerKeyMd5"`
	// [string] The path to the file to upload.
	Source *string `pulumi:"source"`
	// [string] The storage class of the object. Valid value is STANDARD. Default is STANDARD.
	StorageClass *string `pulumi:"storageClass"`
	// [map] The tag-set for the object.
	Tags map[string]string `pulumi:"tags"`
	// [string] The version of the object.
	VersionId *string `pulumi:"versionId"`
	// [string] Redirects requests for this object to another object in the same bucket or to an external URL.
	WebsiteRedirect *string `pulumi:"websiteRedirect"`
}

type ObjectState struct {
	// [string] The name of the bucket where the object will be stored. Must be between 3 and 63 characters.
	Bucket pulumi.StringPtrInput
	// [string] Specifies caching behavior along the request/reply chain.
	CacheControl pulumi.StringPtrInput
	// [string] Inline content of the object.
	Content pulumi.StringPtrInput
	// [string] Specifies presentational information for the object.
	ContentDisposition pulumi.StringPtrInput
	// [string] Specifies what content encodings have been applied to the object.
	ContentEncoding pulumi.StringPtrInput
	// [string] The natural language or languages of the intended audience for the object.
	ContentLanguage pulumi.StringPtrInput
	// [string] A standard MIME type describing the format of the contents.
	ContentType pulumi.StringPtrInput
	// [string] An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.
	Etag pulumi.StringPtrInput
	// [string] The date and time at which the object is no longer cacheable.
	Expires pulumi.StringPtrInput
	// [bool] If true, the object will be destroyed if versioning is enabled then all versions will be destroyed. Default is `false`.
	ForceDestroy pulumi.BoolPtrInput
	// [string] The key of the object. Must be at least 1 character long.
	Key pulumi.StringPtrInput
	// [map] A map of metadata to store with the object in IONOS Object Storage. Metadata keys must be lowercase alphanumeric characters.
	Metadata pulumi.StringMapInput
	// [string]The concatenation of the authentication device's serial number, a space, and the value displayed on your authentication device.
	Mfa pulumi.StringPtrInput
	// [string] Indicates whether a legal hold is in effect for the object. Valid values are `ON` and `OFF`.
	ObjectLockLegalHold pulumi.StringPtrInput
	// [string] The object lock mode that you want to apply to the object. Valid values are `GOVERNANCE` and `COMPLIANCE`.
	ObjectLockMode pulumi.StringPtrInput
	// [string] The date and time when the object lock retention expires.Must be in RFC3999 format
	ObjectLockRetainUntilDate pulumi.StringPtrInput
	// [string] Confirms that the requester knows that they will be charged for the request.
	RequestPayer pulumi.StringPtrInput
	// [string] The server-side encryption algorithm used when storing this object in IONOS Object Storage. Valid value is AES256.
	ServerSideEncryption pulumi.StringPtrInput
	// [string] Specifies the IONOS Object Storage Encryption Context for object encryption.
	ServerSideEncryptionContext pulumi.StringPtrInput
	// [string] Specifies the algorithm to use for encrypting the object. Valid value is AES256.
	ServerSideEncryptionCustomerAlgorithm pulumi.StringPtrInput
	// [string] Specifies the 256-bit, base64-encoded encryption key to use to encrypt and decrypt your data.
	ServerSideEncryptionCustomerKey pulumi.StringPtrInput
	// [string] Specifies the 128-bit MD5 digest of the encryption key.
	ServerSideEncryptionCustomerKeyMd5 pulumi.StringPtrInput
	// [string] The path to the file to upload.
	Source pulumi.StringPtrInput
	// [string] The storage class of the object. Valid value is STANDARD. Default is STANDARD.
	StorageClass pulumi.StringPtrInput
	// [map] The tag-set for the object.
	Tags pulumi.StringMapInput
	// [string] The version of the object.
	VersionId pulumi.StringPtrInput
	// [string] Redirects requests for this object to another object in the same bucket or to an external URL.
	WebsiteRedirect pulumi.StringPtrInput
}

func (ObjectState) ElementType() reflect.Type {
	return reflect.TypeOf((*objectState)(nil)).Elem()
}

type objectArgs struct {
	// [string] The name of the bucket where the object will be stored. Must be between 3 and 63 characters.
	Bucket string `pulumi:"bucket"`
	// [string] Specifies caching behavior along the request/reply chain.
	CacheControl *string `pulumi:"cacheControl"`
	// [string] Inline content of the object.
	Content *string `pulumi:"content"`
	// [string] Specifies presentational information for the object.
	ContentDisposition *string `pulumi:"contentDisposition"`
	// [string] Specifies what content encodings have been applied to the object.
	ContentEncoding *string `pulumi:"contentEncoding"`
	// [string] The natural language or languages of the intended audience for the object.
	ContentLanguage *string `pulumi:"contentLanguage"`
	// [string] A standard MIME type describing the format of the contents.
	ContentType *string `pulumi:"contentType"`
	// [string] The date and time at which the object is no longer cacheable.
	Expires *string `pulumi:"expires"`
	// [bool] If true, the object will be destroyed if versioning is enabled then all versions will be destroyed. Default is `false`.
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// [string] The key of the object. Must be at least 1 character long.
	Key string `pulumi:"key"`
	// [map] A map of metadata to store with the object in IONOS Object Storage. Metadata keys must be lowercase alphanumeric characters.
	Metadata map[string]string `pulumi:"metadata"`
	// [string]The concatenation of the authentication device's serial number, a space, and the value displayed on your authentication device.
	Mfa *string `pulumi:"mfa"`
	// [string] Indicates whether a legal hold is in effect for the object. Valid values are `ON` and `OFF`.
	ObjectLockLegalHold *string `pulumi:"objectLockLegalHold"`
	// [string] The object lock mode that you want to apply to the object. Valid values are `GOVERNANCE` and `COMPLIANCE`.
	ObjectLockMode *string `pulumi:"objectLockMode"`
	// [string] The date and time when the object lock retention expires.Must be in RFC3999 format
	ObjectLockRetainUntilDate *string `pulumi:"objectLockRetainUntilDate"`
	// [string] Confirms that the requester knows that they will be charged for the request.
	RequestPayer *string `pulumi:"requestPayer"`
	// [string] The server-side encryption algorithm used when storing this object in IONOS Object Storage. Valid value is AES256.
	ServerSideEncryption *string `pulumi:"serverSideEncryption"`
	// [string] Specifies the IONOS Object Storage Encryption Context for object encryption.
	ServerSideEncryptionContext *string `pulumi:"serverSideEncryptionContext"`
	// [string] Specifies the algorithm to use for encrypting the object. Valid value is AES256.
	ServerSideEncryptionCustomerAlgorithm *string `pulumi:"serverSideEncryptionCustomerAlgorithm"`
	// [string] Specifies the 256-bit, base64-encoded encryption key to use to encrypt and decrypt your data.
	ServerSideEncryptionCustomerKey *string `pulumi:"serverSideEncryptionCustomerKey"`
	// [string] Specifies the 128-bit MD5 digest of the encryption key.
	ServerSideEncryptionCustomerKeyMd5 *string `pulumi:"serverSideEncryptionCustomerKeyMd5"`
	// [string] The path to the file to upload.
	Source *string `pulumi:"source"`
	// [string] The storage class of the object. Valid value is STANDARD. Default is STANDARD.
	StorageClass *string `pulumi:"storageClass"`
	// [map] The tag-set for the object.
	Tags map[string]string `pulumi:"tags"`
	// [string] Redirects requests for this object to another object in the same bucket or to an external URL.
	WebsiteRedirect *string `pulumi:"websiteRedirect"`
}

// The set of arguments for constructing a Object resource.
type ObjectArgs struct {
	// [string] The name of the bucket where the object will be stored. Must be between 3 and 63 characters.
	Bucket pulumi.StringInput
	// [string] Specifies caching behavior along the request/reply chain.
	CacheControl pulumi.StringPtrInput
	// [string] Inline content of the object.
	Content pulumi.StringPtrInput
	// [string] Specifies presentational information for the object.
	ContentDisposition pulumi.StringPtrInput
	// [string] Specifies what content encodings have been applied to the object.
	ContentEncoding pulumi.StringPtrInput
	// [string] The natural language or languages of the intended audience for the object.
	ContentLanguage pulumi.StringPtrInput
	// [string] A standard MIME type describing the format of the contents.
	ContentType pulumi.StringPtrInput
	// [string] The date and time at which the object is no longer cacheable.
	Expires pulumi.StringPtrInput
	// [bool] If true, the object will be destroyed if versioning is enabled then all versions will be destroyed. Default is `false`.
	ForceDestroy pulumi.BoolPtrInput
	// [string] The key of the object. Must be at least 1 character long.
	Key pulumi.StringInput
	// [map] A map of metadata to store with the object in IONOS Object Storage. Metadata keys must be lowercase alphanumeric characters.
	Metadata pulumi.StringMapInput
	// [string]The concatenation of the authentication device's serial number, a space, and the value displayed on your authentication device.
	Mfa pulumi.StringPtrInput
	// [string] Indicates whether a legal hold is in effect for the object. Valid values are `ON` and `OFF`.
	ObjectLockLegalHold pulumi.StringPtrInput
	// [string] The object lock mode that you want to apply to the object. Valid values are `GOVERNANCE` and `COMPLIANCE`.
	ObjectLockMode pulumi.StringPtrInput
	// [string] The date and time when the object lock retention expires.Must be in RFC3999 format
	ObjectLockRetainUntilDate pulumi.StringPtrInput
	// [string] Confirms that the requester knows that they will be charged for the request.
	RequestPayer pulumi.StringPtrInput
	// [string] The server-side encryption algorithm used when storing this object in IONOS Object Storage. Valid value is AES256.
	ServerSideEncryption pulumi.StringPtrInput
	// [string] Specifies the IONOS Object Storage Encryption Context for object encryption.
	ServerSideEncryptionContext pulumi.StringPtrInput
	// [string] Specifies the algorithm to use for encrypting the object. Valid value is AES256.
	ServerSideEncryptionCustomerAlgorithm pulumi.StringPtrInput
	// [string] Specifies the 256-bit, base64-encoded encryption key to use to encrypt and decrypt your data.
	ServerSideEncryptionCustomerKey pulumi.StringPtrInput
	// [string] Specifies the 128-bit MD5 digest of the encryption key.
	ServerSideEncryptionCustomerKeyMd5 pulumi.StringPtrInput
	// [string] The path to the file to upload.
	Source pulumi.StringPtrInput
	// [string] The storage class of the object. Valid value is STANDARD. Default is STANDARD.
	StorageClass pulumi.StringPtrInput
	// [map] The tag-set for the object.
	Tags pulumi.StringMapInput
	// [string] Redirects requests for this object to another object in the same bucket or to an external URL.
	WebsiteRedirect pulumi.StringPtrInput
}

func (ObjectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*objectArgs)(nil)).Elem()
}

type ObjectInput interface {
	pulumi.Input

	ToObjectOutput() ObjectOutput
	ToObjectOutputWithContext(ctx context.Context) ObjectOutput
}

func (*Object) ElementType() reflect.Type {
	return reflect.TypeOf((**Object)(nil)).Elem()
}

func (i *Object) ToObjectOutput() ObjectOutput {
	return i.ToObjectOutputWithContext(context.Background())
}

func (i *Object) ToObjectOutputWithContext(ctx context.Context) ObjectOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectOutput)
}

// ObjectArrayInput is an input type that accepts ObjectArray and ObjectArrayOutput values.
// You can construct a concrete instance of `ObjectArrayInput` via:
//
//	ObjectArray{ ObjectArgs{...} }
type ObjectArrayInput interface {
	pulumi.Input

	ToObjectArrayOutput() ObjectArrayOutput
	ToObjectArrayOutputWithContext(context.Context) ObjectArrayOutput
}

type ObjectArray []ObjectInput

func (ObjectArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Object)(nil)).Elem()
}

func (i ObjectArray) ToObjectArrayOutput() ObjectArrayOutput {
	return i.ToObjectArrayOutputWithContext(context.Background())
}

func (i ObjectArray) ToObjectArrayOutputWithContext(ctx context.Context) ObjectArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectArrayOutput)
}

// ObjectMapInput is an input type that accepts ObjectMap and ObjectMapOutput values.
// You can construct a concrete instance of `ObjectMapInput` via:
//
//	ObjectMap{ "key": ObjectArgs{...} }
type ObjectMapInput interface {
	pulumi.Input

	ToObjectMapOutput() ObjectMapOutput
	ToObjectMapOutputWithContext(context.Context) ObjectMapOutput
}

type ObjectMap map[string]ObjectInput

func (ObjectMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Object)(nil)).Elem()
}

func (i ObjectMap) ToObjectMapOutput() ObjectMapOutput {
	return i.ToObjectMapOutputWithContext(context.Background())
}

func (i ObjectMap) ToObjectMapOutputWithContext(ctx context.Context) ObjectMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectMapOutput)
}

type ObjectOutput struct{ *pulumi.OutputState }

func (ObjectOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Object)(nil)).Elem()
}

func (o ObjectOutput) ToObjectOutput() ObjectOutput {
	return o
}

func (o ObjectOutput) ToObjectOutputWithContext(ctx context.Context) ObjectOutput {
	return o
}

// [string] The name of the bucket where the object will be stored. Must be between 3 and 63 characters.
func (o ObjectOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v *Object) pulumi.StringOutput { return v.Bucket }).(pulumi.StringOutput)
}

// [string] Specifies caching behavior along the request/reply chain.
func (o ObjectOutput) CacheControl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.CacheControl }).(pulumi.StringPtrOutput)
}

// [string] Inline content of the object.
func (o ObjectOutput) Content() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.Content }).(pulumi.StringPtrOutput)
}

// [string] Specifies presentational information for the object.
func (o ObjectOutput) ContentDisposition() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ContentDisposition }).(pulumi.StringPtrOutput)
}

// [string] Specifies what content encodings have been applied to the object.
func (o ObjectOutput) ContentEncoding() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ContentEncoding }).(pulumi.StringPtrOutput)
}

// [string] The natural language or languages of the intended audience for the object.
func (o ObjectOutput) ContentLanguage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ContentLanguage }).(pulumi.StringPtrOutput)
}

// [string] A standard MIME type describing the format of the contents.
func (o ObjectOutput) ContentType() pulumi.StringOutput {
	return o.ApplyT(func(v *Object) pulumi.StringOutput { return v.ContentType }).(pulumi.StringOutput)
}

// [string] An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.
func (o ObjectOutput) Etag() pulumi.StringOutput {
	return o.ApplyT(func(v *Object) pulumi.StringOutput { return v.Etag }).(pulumi.StringOutput)
}

// [string] The date and time at which the object is no longer cacheable.
func (o ObjectOutput) Expires() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.Expires }).(pulumi.StringPtrOutput)
}

// [bool] If true, the object will be destroyed if versioning is enabled then all versions will be destroyed. Default is `false`.
func (o ObjectOutput) ForceDestroy() pulumi.BoolOutput {
	return o.ApplyT(func(v *Object) pulumi.BoolOutput { return v.ForceDestroy }).(pulumi.BoolOutput)
}

// [string] The key of the object. Must be at least 1 character long.
func (o ObjectOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *Object) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

// [map] A map of metadata to store with the object in IONOS Object Storage. Metadata keys must be lowercase alphanumeric characters.
func (o ObjectOutput) Metadata() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Object) pulumi.StringMapOutput { return v.Metadata }).(pulumi.StringMapOutput)
}

// [string]The concatenation of the authentication device's serial number, a space, and the value displayed on your authentication device.
func (o ObjectOutput) Mfa() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.Mfa }).(pulumi.StringPtrOutput)
}

// [string] Indicates whether a legal hold is in effect for the object. Valid values are `ON` and `OFF`.
func (o ObjectOutput) ObjectLockLegalHold() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ObjectLockLegalHold }).(pulumi.StringPtrOutput)
}

// [string] The object lock mode that you want to apply to the object. Valid values are `GOVERNANCE` and `COMPLIANCE`.
func (o ObjectOutput) ObjectLockMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ObjectLockMode }).(pulumi.StringPtrOutput)
}

// [string] The date and time when the object lock retention expires.Must be in RFC3999 format
func (o ObjectOutput) ObjectLockRetainUntilDate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ObjectLockRetainUntilDate }).(pulumi.StringPtrOutput)
}

// [string] Confirms that the requester knows that they will be charged for the request.
func (o ObjectOutput) RequestPayer() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.RequestPayer }).(pulumi.StringPtrOutput)
}

// [string] The server-side encryption algorithm used when storing this object in IONOS Object Storage. Valid value is AES256.
func (o ObjectOutput) ServerSideEncryption() pulumi.StringOutput {
	return o.ApplyT(func(v *Object) pulumi.StringOutput { return v.ServerSideEncryption }).(pulumi.StringOutput)
}

// [string] Specifies the IONOS Object Storage Encryption Context for object encryption.
func (o ObjectOutput) ServerSideEncryptionContext() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ServerSideEncryptionContext }).(pulumi.StringPtrOutput)
}

// [string] Specifies the algorithm to use for encrypting the object. Valid value is AES256.
func (o ObjectOutput) ServerSideEncryptionCustomerAlgorithm() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ServerSideEncryptionCustomerAlgorithm }).(pulumi.StringPtrOutput)
}

// [string] Specifies the 256-bit, base64-encoded encryption key to use to encrypt and decrypt your data.
func (o ObjectOutput) ServerSideEncryptionCustomerKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ServerSideEncryptionCustomerKey }).(pulumi.StringPtrOutput)
}

// [string] Specifies the 128-bit MD5 digest of the encryption key.
func (o ObjectOutput) ServerSideEncryptionCustomerKeyMd5() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.ServerSideEncryptionCustomerKeyMd5 }).(pulumi.StringPtrOutput)
}

// [string] The path to the file to upload.
func (o ObjectOutput) Source() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.Source }).(pulumi.StringPtrOutput)
}

// [string] The storage class of the object. Valid value is STANDARD. Default is STANDARD.
func (o ObjectOutput) StorageClass() pulumi.StringOutput {
	return o.ApplyT(func(v *Object) pulumi.StringOutput { return v.StorageClass }).(pulumi.StringOutput)
}

// [map] The tag-set for the object.
func (o ObjectOutput) Tags() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Object) pulumi.StringMapOutput { return v.Tags }).(pulumi.StringMapOutput)
}

// [string] The version of the object.
func (o ObjectOutput) VersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *Object) pulumi.StringOutput { return v.VersionId }).(pulumi.StringOutput)
}

// [string] Redirects requests for this object to another object in the same bucket or to an external URL.
func (o ObjectOutput) WebsiteRedirect() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Object) pulumi.StringPtrOutput { return v.WebsiteRedirect }).(pulumi.StringPtrOutput)
}

type ObjectArrayOutput struct{ *pulumi.OutputState }

func (ObjectArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Object)(nil)).Elem()
}

func (o ObjectArrayOutput) ToObjectArrayOutput() ObjectArrayOutput {
	return o
}

func (o ObjectArrayOutput) ToObjectArrayOutputWithContext(ctx context.Context) ObjectArrayOutput {
	return o
}

func (o ObjectArrayOutput) Index(i pulumi.IntInput) ObjectOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Object {
		return vs[0].([]*Object)[vs[1].(int)]
	}).(ObjectOutput)
}

type ObjectMapOutput struct{ *pulumi.OutputState }

func (ObjectMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Object)(nil)).Elem()
}

func (o ObjectMapOutput) ToObjectMapOutput() ObjectMapOutput {
	return o
}

func (o ObjectMapOutput) ToObjectMapOutputWithContext(ctx context.Context) ObjectMapOutput {
	return o
}

func (o ObjectMapOutput) MapIndex(k pulumi.StringInput) ObjectOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Object {
		return vs[0].(map[string]*Object)[vs[1].(string)]
	}).(ObjectOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ObjectInput)(nil)).Elem(), &Object{})
	pulumi.RegisterInputType(reflect.TypeOf((*ObjectArrayInput)(nil)).Elem(), ObjectArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ObjectMapInput)(nil)).Elem(), ObjectMap{})
	pulumi.RegisterOutputType(ObjectOutput{})
	pulumi.RegisterOutputType(ObjectArrayOutput{})
	pulumi.RegisterOutputType(ObjectMapOutput{})
}

// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "ionoscloud:index/apigateway:Apigateway":
		r = &Apigateway{}
	case "ionoscloud:index/apigatewayRoute:ApigatewayRoute":
		r = &ApigatewayRoute{}
	case "ionoscloud:index/applicationLoadbalancer:ApplicationLoadbalancer":
		r = &ApplicationLoadbalancer{}
	case "ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule":
		r = &ApplicationLoadbalancerForwardingrule{}
	case "ionoscloud:index/autoCertificate:AutoCertificate":
		r = &AutoCertificate{}
	case "ionoscloud:index/autoCertificateProvider:AutoCertificateProvider":
		r = &AutoCertificateProvider{}
	case "ionoscloud:index/autoscalingGroup:AutoscalingGroup":
		r = &AutoscalingGroup{}
	case "ionoscloud:index/certificate:Certificate":
		r = &Certificate{}
	case "ionoscloud:index/kafkaCluster:KafkaCluster":
		r = &KafkaCluster{}
	case "ionoscloud:index/kafkaClusterTopic:KafkaClusterTopic":
		r = &KafkaClusterTopic{}
	case "ionoscloud:index/loadbalancer:Loadbalancer":
		r = &Loadbalancer{}
	case "ionoscloud:index/loggingPipeline:LoggingPipeline":
		r = &LoggingPipeline{}
	case "ionoscloud:index/natgateway:Natgateway":
		r = &Natgateway{}
	case "ionoscloud:index/natgatewayRule:NatgatewayRule":
		r = &NatgatewayRule{}
	case "ionoscloud:index/networkloadbalancer:Networkloadbalancer":
		r = &Networkloadbalancer{}
	case "ionoscloud:index/networkloadbalancerForwardingrule:NetworkloadbalancerForwardingrule":
		r = &NetworkloadbalancerForwardingrule{}
	case "ionoscloud:index/serverBootDeviceSelection:ServerBootDeviceSelection":
		r = &ServerBootDeviceSelection{}
	case "ionoscloud:index/targetGroup:TargetGroup":
		r = &TargetGroup{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:ionoscloud" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/apigateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/apigatewayRoute",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/applicationLoadbalancer",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/applicationLoadbalancerForwardingrule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/autoCertificate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/autoCertificateProvider",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/autoscalingGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/certificate",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/kafkaCluster",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/kafkaClusterTopic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/loadbalancer",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/loggingPipeline",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/natgateway",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/natgatewayRule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/networkloadbalancer",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/networkloadbalancerForwardingrule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/serverBootDeviceSelection",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"index/targetGroup",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"ionoscloud",
		&pkg{version},
	)
}

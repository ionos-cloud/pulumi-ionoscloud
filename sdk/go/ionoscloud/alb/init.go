// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package alb

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
	case "ionoscloud:alb/applicationLoadbalancer:ApplicationLoadbalancer":
		r = &ApplicationLoadbalancer{}
	case "ionoscloud:alb/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule":
		r = &ApplicationLoadbalancerForwardingrule{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"alb/applicationLoadbalancer",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"alb/applicationLoadbalancerForwardingrule",
		&module{version},
	)
}

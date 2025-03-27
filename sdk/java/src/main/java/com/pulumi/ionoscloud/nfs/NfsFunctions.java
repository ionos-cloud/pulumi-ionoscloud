// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.nfs;

import com.pulumi.core.Output;
import com.pulumi.core.TypeShape;
import com.pulumi.deployment.Deployment;
import com.pulumi.deployment.InvokeOptions;
import com.pulumi.deployment.InvokeOutputOptions;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.nfs.inputs.GetClusterArgs;
import com.pulumi.ionoscloud.nfs.inputs.GetClusterPlainArgs;
import com.pulumi.ionoscloud.nfs.inputs.GetShareArgs;
import com.pulumi.ionoscloud.nfs.inputs.GetSharePlainArgs;
import com.pulumi.ionoscloud.nfs.outputs.GetClusterResult;
import com.pulumi.ionoscloud.nfs.outputs.GetShareResult;
import java.util.concurrent.CompletableFuture;

public final class NfsFunctions {
    /**
     * Returns information about clusters of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetClusterArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getCluster(GetClusterArgs.builder()
     *             .location("location")
     *             .id("cluster-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetClusterResult> getCluster(GetClusterArgs args) {
        return getCluster(args, InvokeOptions.Empty);
    }
    /**
     * Returns information about clusters of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetClusterArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getCluster(GetClusterArgs.builder()
     *             .location("location")
     *             .id("cluster-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetClusterResult> getClusterPlain(GetClusterPlainArgs args) {
        return getClusterPlain(args, InvokeOptions.Empty);
    }
    /**
     * Returns information about clusters of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetClusterArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getCluster(GetClusterArgs.builder()
     *             .location("location")
     *             .id("cluster-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetClusterResult> getCluster(GetClusterArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("ionoscloud:nfs/getCluster:getCluster", TypeShape.of(GetClusterResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Returns information about clusters of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetClusterArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getCluster(GetClusterArgs.builder()
     *             .location("location")
     *             .id("cluster-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetClusterResult> getCluster(GetClusterArgs args, InvokeOutputOptions options) {
        return Deployment.getInstance().invoke("ionoscloud:nfs/getCluster:getCluster", TypeShape.of(GetClusterResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Returns information about clusters of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetClusterArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getCluster(GetClusterArgs.builder()
     *             .location("location")
     *             .id("cluster-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetClusterResult> getClusterPlain(GetClusterPlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("ionoscloud:nfs/getCluster:getCluster", TypeShape.of(GetClusterResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Returns information about shares of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetShareArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getShare(GetShareArgs.builder()
     *             .location("location")
     *             .clusterId("cluster-id")
     *             .id("share-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetShareResult> getShare(GetShareArgs args) {
        return getShare(args, InvokeOptions.Empty);
    }
    /**
     * Returns information about shares of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetShareArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getShare(GetShareArgs.builder()
     *             .location("location")
     *             .clusterId("cluster-id")
     *             .id("share-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetShareResult> getSharePlain(GetSharePlainArgs args) {
        return getSharePlain(args, InvokeOptions.Empty);
    }
    /**
     * Returns information about shares of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetShareArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getShare(GetShareArgs.builder()
     *             .location("location")
     *             .clusterId("cluster-id")
     *             .id("share-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetShareResult> getShare(GetShareArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("ionoscloud:nfs/getShare:getShare", TypeShape.of(GetShareResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Returns information about shares of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetShareArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getShare(GetShareArgs.builder()
     *             .location("location")
     *             .clusterId("cluster-id")
     *             .id("share-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetShareResult> getShare(GetShareArgs args, InvokeOutputOptions options) {
        return Deployment.getInstance().invoke("ionoscloud:nfs/getShare:getShare", TypeShape.of(GetShareResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Returns information about shares of Network File Storage (NFS) on IonosCloud.
     * 
     * ## By ID
     * 
     * &lt;!--Start PulumiCodeChooser --&gt;
     * <pre>
     * {@code
     * package generated_program;
     * 
     * import com.pulumi.Context;
     * import com.pulumi.Pulumi;
     * import com.pulumi.core.Output;
     * import com.pulumi.ionoscloud.nfs.NfsFunctions;
     * import com.pulumi.ionoscloud.nfs.inputs.GetShareArgs;
     * import java.util.List;
     * import java.util.ArrayList;
     * import java.util.Map;
     * import java.io.File;
     * import java.nio.file.Files;
     * import java.nio.file.Paths;
     * 
     * public class App {
     *     public static void main(String[] args) {
     *         Pulumi.run(App::stack);
     *     }
     * 
     *     public static void stack(Context ctx) {
     *         final var example = NfsFunctions.getShare(GetShareArgs.builder()
     *             .location("location")
     *             .clusterId("cluster-id")
     *             .id("share-id")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetShareResult> getSharePlain(GetSharePlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("ionoscloud:nfs/getShare:getShare", TypeShape.of(GetShareResult.class), args, Utilities.withVersion(options));
    }
}

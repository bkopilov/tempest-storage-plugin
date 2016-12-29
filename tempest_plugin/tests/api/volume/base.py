
import tempest.api.volume.base as base_tempest_volume
from tempest_storage_plugin.tempest_plugin.tests import clients


class BaseVolumeTest(base_tempest_volume.BaseVolumeTest):
    @classmethod
    def skip_checks(cls):
        super(BaseVolumeTest, cls).skip_checks()

    @classmethod
    def setup_credentials(cls):
        super(BaseVolumeTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(BaseVolumeTest, cls).setup_clients()
        cls._setup_clients("primary")

    @classmethod
    def resource_setup(cls):
        super(BaseVolumeTest, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(BaseVolumeTest, cls).resource_cleanup()

    @classmethod
    def _setup_clients(cls, credential_type):
        if credential_type == "admin":
            manager = clients.Manager(auth_provider=cls.os_adm.auth_provider,
                                      service="volume", region="RegionOne")
            cls.admin_availability_zone_v3_client = manager.availability_zone_v3_client
            cls.admin_volumes_v3_client = manager.volumes_v3_client
            cls.admin_backups_v3_client = manager.backups_v3_client
            cls.admin_services_v3_client = manager.services_v3_client
            cls.admin_volumes_extension_v3_client = manager.volumes_extension_v3_client
            cls.admin_volume_limits_v3_client = manager.volume_limits_v3_client
            cls.admin_snapshots_v3_client = manager.snapshots_v3_client
            cls.admin_scheduler_stats_v3_client = manager.scheduler_stats_v3_client
            cls.admin_volume_qos_v3_client = manager.volume_qos_v3_client
            cls.admin_volume_types_v3_client = manager.volume_types_v3_client
            cls.admin_hosts_v3_client = manager.hosts_v3_client
            cls.admin_encryption_types_v3_client = manager.encryption_types_v3_client
            cls.admin_quotas_v3_client = manager.quotas_v3_client
            cls.admin_capabilities_v3_client = manager.capabilities_v3_client

        elif credential_type == "primary":
            manager = clients.Manager(auth_provider=cls.os.auth_provider,
                                      service="volume", region="RegionOne")
            cls.availability_zone_v3_client = manager.availability_zone_v3_client
            cls.volumes_v3_client = manager.volumes_v3_client
            cls.backups_v3_client = manager.backups_v3_client
            cls.services_v3_client = manager.services_v3_client
            cls.volumes_extension_v3_client = manager.volumes_extension_v3_client
            cls.volume_limits_v3_client = manager.volume_limits_v3_client
            cls.snapshots_v3_client = manager.snapshots_v3_client
            cls.scheduler_stats_v3_client = manager.scheduler_stats_v3_client
            cls.volume_qos_v3_client = manager.volume_qos_v3_client
            cls.volume_types_v3_client = manager.volume_types_v3_client
            cls.hosts_v3_client = manager.hosts_v3_client
            cls.encryption_types_v3_client = manager.encryption_types_v3_client
            cls.quotas_v3_client = manager.quotas_v3_client
            cls.capabilities_v3_client = manager.capabilities_v3_client


class BaseVolumeAdminTest(base_tempest_volume.BaseVolumeAdminTest):
    @classmethod
    def skip_checks(cls):
        super(BaseVolumeAdminTest, cls).skip_checks()

    @classmethod
    def setup_credentials(cls):
        super(BaseVolumeAdminTest, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(BaseVolumeAdminTest, cls).setup_clients()
        cls._setup_clients(credential_type="admin")
        cls._setup_clients(credential_type="primary")

    @classmethod
    def resource_setup(cls):
        super(BaseVolumeAdminTest, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(BaseVolumeAdminTest, cls).resource_cleanup()

    @classmethod
    def _setup_clients(cls, credential_type):
        if credential_type == "admin":
            manager = clients.Manager(auth_provider=cls.os_adm.auth_provider,
                                      service="volume", region="RegionOne")
            cls.admin_availability_zone_v3_client = manager.availability_zone_v3_client
            cls.admin_volumes_v3_client = manager.volumes_v3_client
            cls.admin_backups_v3_client = manager.backups_v3_client
            cls.admin_services_v3_client = manager.services_v3_client
            cls.admin_volumes_extension_v3_client = manager.volumes_extension_v3_client
            cls.admin_volume_limits_v3_client = manager.volume_limits_v3_client
            cls.admin_snapshots_v3_client = manager.snapshots_v3_client
            cls.admin_scheduler_stats_v3_client = manager.scheduler_stats_v3_client
            cls.admin_volume_qos_v3_client = manager.volume_qos_v3_client
            cls.admin_volume_types_v3_client = manager.volume_types_v3_client
            cls.admin_hosts_v3_client = manager.hosts_v3_client
            cls.admin_encryption_types_v3_client = manager.encryption_types_v3_client
            cls.admin_quotas_v3_client = manager.quotas_v3_client
            cls.admin_capabilities_v3_client = manager.capabilities_v3_client

        elif credential_type == "primary":
            manager = clients.Manager(auth_provider=cls.os.auth_provider,
                                      service="volume", region="RegionOne")
            cls.availability_zone_v3_client = manager.availability_zone_v3_client
            cls.volumes_v3_client = manager.volumes_v3_client
            cls.backups_v3_client = manager.backups_v3_client
            cls.services_v3_client = manager.services_v3_client
            cls.volumes_extension_v3_client = manager.volumes_extension_v3_client
            cls.volume_limits_v3_client = manager.volume_limits_v3_client
            cls.snapshots_v3_client = manager.snapshots_v3_client
            cls.scheduler_stats_v3_client = manager.scheduler_stats_v3_client
            cls.volume_qos_v3_client = manager.volume_qos_v3_client
            cls.volume_types_v3_client = manager.volume_types_v3_client
            cls.hosts_v3_client = manager.hosts_v3_client
            cls.encryption_types_v3_client = manager.encryption_types_v3_client
            cls.quotas_v3_client = manager.quotas_v3_client
            cls.capabilities_v3_client = manager.capabilities_v3_client


from tempest.scenario import manager as scenario_tempest_manager


class ScenarioTest(scenario_tempest_manager.ScenarioTest):
    @classmethod
    def setup_clients(cls):
        super(ScenarioTest, cls).setup_clients()


class NetworkScenarioTest(scenario_tempest_manager.NetworkScenarioTest):
    @classmethod
    def setup_clients(cls):
        super(ScenarioTest, cls).setup_clients()


class EncryptionScenarioTest(scenario_tempest_manager.EncryptionScenarioTest):
    @classmethod
    def setup_clients(cls):
        super(EncryptionScenarioTest, cls).setup_clients()


class ObjectStorageScenarioTest(scenario_tempest_manager.
                                ObjectStorageScenarioTest):

    @classmethod
    def setup_clients(cls):
        super(ObjectStorageScenarioTest, cls).setup_clients()

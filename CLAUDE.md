# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment

### Build & Test Commands
- **Install**: `pip install -e .`
- **Build**: `python setup.py build`
- **Run all tests**: `python -m test.test`
- **Run single test**: `python -m test.test_ipfs_kit` or `python -m test.test_storacha_kit`
- **Run API server**: `uvicorn ipfs_kit_py.api:app --reload --port 8000`
- **Generate AST**: `python -m astroid ipfs_kit_py > ast_analysis.json`
- **Check for duplications**: `pylint --disable=all --enable=duplicate-code ipfs_kit_py`

### Development Guidelines
- **Test-First Development**: All new features must first be developed in the test/ folder
- **Feature Isolation**: Do not modify code outside of test/ until fully debugged
- **API Exposure**: All functionality should be exposed via FastAPI endpoints
- **Performance Focus**: Use memory-mapped structures and Arrow C Data Interface for low-latency IPC
- **Code Analysis**: Maintain an abstract syntax tree (AST) of the project to identify and prevent code duplication
- **DRY Principle**: Use the AST to enforce Don't Repeat Yourself by detecting similar code structures

### Testing Strategy

The project follows a comprehensive testing approach to ensure reliability and maintainability:

#### Test Organization
- **Unit Tests**: Located in the `test/` directory with file naming pattern `test_*.py`
- **Integration Tests**: Also in `test/` but focused on component interactions
- **Performance Tests**: Specialized tests for measuring throughput and latency

#### Recent Test Improvements
- **Mock Integration**: Fixed PyArrow mocking for cluster state helpers
- **Role-Based Architecture**: Improved fixtures for master/worker/leecher node testing
- **Gateway Compatibility**: Enhanced testing with proper filesystem interface mocking
- **LibP2P Integration**: Fixed tests to work without external dependencies
- **Parameter Validation**: Corrected constructor argument handling in tests
- **Interface Focus**: Made tests more resilient to implementation changes by focusing on behaviors rather than implementation details

#### Test Patterns
1. **Fixture-Based Testing**: Use pytest fixtures for test setup and teardown
2. **Mocking IPFS Daemon**: Use subprocess mocking to avoid actual daemon dependency
3. **Property-Based Testing**: Use hypothesis for edge case discovery
4. **Snapshot Testing**: For configuration and schema verification
5. **Parallelized Test Execution**: For faster feedback cycles
6. **PyArrow Patching**: Special handling for PyArrow Schema objects and Table methods
7. **Logging Suppression**: Context managers to control test output noise

#### PyArrow Testing Strategy
The tests must handle PyArrow's immutable Schema objects during mocking. Key approaches:

1. **MonkeyPatching**: Using pytest's monkeypatch fixture to safely patch immutable types
2. **Schema Equality Override**: Custom equality checks that handle MagicMock objects
3. **Schema Type Conversion**: Automatic conversion from MagicMock schemas to real PyArrow schemas
4. **Error Handling**: Special handling for PyArrow's strict type checking errors
5. **Cleanup Patching**: Custom cleanup methods to prevent errors during test teardown

#### Continuous Integration Integration
- Tests are run on every PR and commit to main branch
- Test reports and coverage metrics are generated automatically
- Performance regression tests compare against baseline benchmarks

## Code Style Guidelines
- **Imports**: Standard library first, third-party next, project imports last
- **Variables/Functions**: Use snake_case
- **Classes**: Use snake_case (this is project-specific, differs from PEP 8)
- **Indentation**: 4 spaces, no tabs
- **Error Handling**: Use try/except blocks, catch specific exceptions when possible
- **No Type Annotations**: Project doesn't use typing hints
- **Docstrings**: Not consistently used

The project is a wrapper around HuggingFace Transformers that adds IPFS model management capabilities, allowing models to be downloaded from HTTP/S3/IPFS based on availability and speed.

### API Integration Points
- **IPFS HTTP API**: REST interface (localhost:5001/api/v0) for core IPFS operations
- **IPFS Cluster API**: REST interface (localhost:9094/api/v0) for cluster coordination
- **IPFS Cluster Proxy**: Proxied IPFS API (localhost:9095/api/v0)
- **IPFS Gateway**: Content retrieval via HTTP (localhost:8080/ipfs/[cid])
- **IPFS Socket Interface**: Unix socket for high-performance local communication (/ip4/127.0.0.1/tcp/4001)
- **IPFS Unix Socket API**: On Linux, Kubo can be configured to expose its API via a Unix domain socket instead of HTTP, providing lower-latency communication for local processes. This can be configured in the IPFS config file by modifying the `API.Addresses` field to include a Unix socket path (e.g., `/unix/path/to/socket`).

These APIs enable creating "swarms of swarms" by allowing distributed clusters to communicate across networks and coordinate content pinning, replication, and routing across organizational boundaries. Socket interfaces provide lower-latency communication for high-performance local operations, with Unix domain sockets being particularly efficient for inter-process communication on the same machine.

## IPFS Core Concepts

The IPFS (InterPlanetary File System) architecture is built on several key concepts and components that are essential to understand for effective implementation:

### Content Addressing
- **Content Identifiers (CIDs)**: Unique fingerprints of content based on cryptographic hashes
- **Multihash Format**: Extensible hashing format supporting multiple hash algorithms (default: SHA-256)
- **Base32/Base58 Encoding**: Human-readable representations of binary CIDs
- **Version Prefixes**: CIDv0 (base58btc-encoded SHA-256) vs CIDv1 (self-describing, supports multicodec)

### Data Structures
- **Merkle DAG (Directed Acyclic Graph)**: Core data structure for content-addressed storage
- **IPLD (InterPlanetary Linked Data)**: Framework for creating data models with content-addressable linking
- **UnixFS**: File system abstraction built on IPLD for representing traditional files/directories
- **Blocks**: Raw data chunks that form the atomic units of the Merkle DAG

### Network Components
- **DHT (Distributed Hash Table)**: Distributed key-value store for content routing
- **Bitswap**: Protocol for exchanging blocks between peers
- **libp2p**: Modular networking stack powering IPFS peer-to-peer communication
- **MultiFormats**: Self-describing protocols, formats, and addressing schemes
- **IPNS (InterPlanetary Name System)**: Mutable naming system for content addressing

### Node Types
- **Full Nodes**: Store and serve content, participate in DHT
- **Gateway Nodes**: Provide HTTP access to IPFS content
- **Client Nodes**: Lightweight nodes that rely on others for content routing/storage
- **Bootstrap Nodes**: Well-known nodes that help new nodes join the network
- **Relay Nodes**: Assist with NAT traversal and indirect connections

### Key Operations
- **Adding Content**: Hash-based deduplication and chunking strategies
- **Retrieving Content**: Resolution process from CID to data
- **Pinning**: Mechanism to prevent content from being garbage collected
- **Publishing**: Making content discoverable through DHT/IPNS
- **Garbage Collection**: Process for reclaiming storage from unpinned content

## Migration Plan: From Old IPFS Kit to New Implementation

### Overview

We need to migrate from the older, deprecated `ipfs_kit` implementation to the new comprehensive `ipfs_kit_py` library. This migration will enhance our capabilities while following the modern architecture that's been established in the new library.

### Current State Analysis
- **Old Implementation**: Basic IPFS functionality with limited role-based architecture (master/worker/leecher)
- **New Implementation**: Comprehensive library with advanced features like tiered caching, metadata indexing, and AI/ML-specific tools

### Migration Strategy

#### Phase 1: Infrastructure Setup (1-2 weeks)
1. **Dependency Installation**
   - Install new ipfs_kit_py with required extras: `pip install ipfs_kit_py[fsspec,arrow,ai_ml]`
   - Set up proper configuration structure using the High-Level API format (YAML/JSON)

2. **Environment Configuration**
   - Create role-based configurations for master/worker/leecher nodes
   - Set up proper file paths for model caching that align with current HuggingFace paths

#### Phase 2: Adapter Layer (2-3 weeks)
1. **Create Compatibility Layer**
   - Implement adapter classes that map old method signatures to new implementation
   - Support backward compatibility for critical operations:
     - `ipfs_add_pin` → `api.pin()`
     - `ipfs_remove_pin` → `api.unpin()`
     - `ipfs_get_pinset` → `api.list_pins()`
     - `load_collection` → mapped to new collection management

2. **Integration with HuggingFace Transformers**
   - Update the `AutoDownloadModel` class to use the new ipfs_kit_py library
   - Retain the same interface for all model-specific classes (ASTModel, AlbertConfig, etc.)

#### Phase 3: Enhanced Features Implementation (3-4 weeks)
1. **Tiered Storage Integration**
   - Implement tiered caching for model files to improve loading speed
   - Configure storage backends for model persistence

2. **Metadata and Search Capabilities**
   - Add metadata indexing for models to enable discovery and versioning
   - Implement search functionality for finding models by tags/attributes

3. **Performance Optimization**
   - Implement parallel downloads for multi-file models
   - Add chunked transfers for large model files

#### Phase 4: Testing and Documentation (2-3 weeks)
1. **Comprehensive Testing**
   - Write tests that validate migration success
   - Ensure backward compatibility for all critical functions
   - Verify performance improvements and measure load time differences

2. **Documentation Updates**
   - Update examples to show both legacy and new preferred approaches
   - Create migration guides for users of the library
   - Document new capabilities and performance benefits

### Implementation Tasks

#### 1. Create IPFSTransformersKit Class
- Develop a new main class that implements the interfaces of both systems
- Use the new ipfs_kit_py High-Level API internally

```python
from ipfs_kit_py.high_level_api import IPFSSimpleAPI

class IPFSTransformersKit:
    """Compatibility layer between old ipfs_kit and new ipfs_kit_py"""
    
    def __init__(self, resources, meta=None):
        # Initialize with compatible parameters
        self.config = {}
        self.role = "leecher"
        
        # Parse legacy meta parameters
        if meta:
            if "role" in meta:
                self.role = meta["role"]
            if "ipfs_path" in meta:
                self.ipfs_path = meta["ipfs_path"]
        
        # Initialize new API
        self.api = IPFSSimpleAPI(
            role=self.role,
            resources=resources or {},
            # Map other parameters as needed
        )
    
    # Implement legacy methods using new API
    def ipfs_add_pin(self, pin, **kwargs):
        return self.api.pin(pin)
    
    def ipfs_remove_pin(self, pin, **kwargs):
        return self.api.unpin(pin)
    
    def load_collection(self, cid, **kwargs):
        # Map to new collection management
        return self.api.get(cid)
    
    # etc...
```

#### 2. Update AutoDownloadModel
- Enhance the existing AutoDownloadModel to use the new capabilities

```python
# Modified version of AutoDownloadModel that uses new ipfs_kit_py
class AutoDownloadModelEnhanced:
    def __init__(self, collection=None, meta=None):
        # Same initialization logic but use new library internally
        from ipfs_kit_py.high_level_api import IPFSSimpleAPI
        
        # Configure paths
        self._configure_paths(meta)
        
        # Initialize API
        self.api = IPFSSimpleAPI(
            role=self.role,
            config={
                "cache": {
                    "disk_path": self.ipfs_path
                }
            }
        )
        
        # Load collection if provided
        if collection:
            # Handle collection loading with new API
            pass
    
    def download(self, **kwargs):
        # Enhanced download using tiered cache and parallel downloads
        # Similar interface to old version
        
        model_name = kwargs.get("model_name")
        cid = kwargs.get("cid")
        
        if model_name:
            # Use new high-performance API for model download
            result = self.api.get(model_name, dest=self.local_path)
            return os.path.join(self.local_path, model_name)
        elif cid:
            # Use new IPFS content retrieval
            result = self.api.get(cid, dest=os.path.join(self.local_path, cid))
            return os.path.join(self.local_path, cid)
```

### Risks and Mitigations

1. **API Incompatibilities**
   - Risk: Some legacy method calls might not map cleanly to new APIs
   - Mitigation: Create adapter functions with full compatibility for all documented functions

2. **Performance Changes**
   - Risk: New library might have different performance characteristics
   - Mitigation: Benchmark before and after, tune cache parameters for optimal performance

3. **Configuration Differences**
   - Risk: Configuration structure differs between old and new systems
   - Mitigation: Create configuration mapping functions and sensible defaults

4. **Dependency Conflicts**
   - Risk: New library might have dependency conflicts with transformers
   - Mitigation: Test with various transformers versions, implement version compatibility checks

### Success Criteria

1. All existing transformer models can be loaded with the same interface
2. Model download speeds meet or exceed previous implementation
3. Test suite passes with both implementations
4. New features (metadata, searching, tiered caching) are available to users who want them

### Timeline

- **Weeks 1-2**: Infrastructure and adapter layer
- **Weeks 3-5**: Core functionality migration and testing
- **Weeks 6-8**: Enhanced features and optimization
- **Weeks 9-10**: Documentation and final testing

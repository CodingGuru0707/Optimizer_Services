# Optimizer Services

## About the Project

Development of a REST API for metallic optimizer service to calculate the cheapest charge mix for an electric arc furnace(EAF).
The charge materials are different scrap types and virgin material. In summary those materials are called commodities. 
The optimization algorithm uses the chemical composition of commodities as input values to guarantee that the chemical composition of the tapped melt is within a specific range.
The melt is tapped after the melting process in the EAF is finished. One complete melting process as well as tapping the melt into a ladle is called a heat.

## Prerequisites

```python
python == 3.5+
django == 3.2
mysql == 8.0.3
djangorestframework == 3.12.4
```
## Project Structure

The project will contain a platform to perform CRUD operations by developing RESTAPI.

It is expected to provide solution for various API methods.
- Get all chemical elements
- Get a commodity by ID
- Update commodity by ID
- Add and remove chemical concentration


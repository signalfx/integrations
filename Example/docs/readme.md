### Metrics documentation instructions

Each integration in this repository must include documentation of the metrics that it emits in a subdirectory called [/docs](./). Here's how to do that. 

1. Create a file with extension .md for every metric emitted by the integration. The name of the file must match the name of the metric. For example, a metric called `gauge.sine` is documented in the file [gauge.sine.md](gauge.sine.md).
  
2. In each `.md` file, include a structured header as follows:
  ```
  ---
  title: A human-understandable title of the metric.
  brief: A brief description of what the metric measures. Specify the unit of
  measurement, such as bytes or percent. 
  metric_type: The type of metric this is. Typically this will be gauge, counter
  or cumulative_counter. 
  ---
  ```

  For example, [gauge.sine.md](gauge.sine.md) contains the following header:
  
  ```
  ---
  title: Sine
  brief: A sine wave
  metric_type: gauge
  ---
  ```
  
3. Below the structured header, include additional information that will help users understand the metric.

  For example, [gauge.sine.md](gauge.sine.md) includes the following usage information that didn't fit in the brief description:
  
  ```
  A sine wave is a curve representing periodic oscillations of constant amplitude
  as given by a sine function.  We send this in as it is a good way to show a
  gauge.
  ```
NOTE: Do not create subdirectories under /docs. The metrics need to all be in /docs so they will be pulled into the product.

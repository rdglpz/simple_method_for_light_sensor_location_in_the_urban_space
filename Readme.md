
# Method for Light Sensor Location in the urban space.

Assuming that the measured luminance data do not have saturation problems, and the environmental-sensitivity data are stored in matrices of the same shape using positive integers, we produce the optimal location map as follows:


1. First, to define the luminance and sensitivity inputs maps as $L$ and $S$ matrices respectively.
2. To compute the weight matrix $W$ using the weighing equation $W = 4^S$. 
3. Then, to calculate the priority matrix $P$ with the Hadamard (element-wise) product using luminance and weight matrices $P = L o W $. 
4. To obtain the list of candidate locations $C$ that  satisfies local optimality in a 4-pixel neighborhood.
  5. To sort the elements in $C$ according to their associated priority value in $P$.
6. To allocate the $n$ sensors in the $n$ locations according to the highest priority.

In the case that the luminance image presents saturation problems, we propose to replace the matrix $L$ by a the Gravitational Luminance Image Representation (GLIR) $G$ and perform the same steps. 

## Gravitational Luminance Image Representation GLIR for saturated nighttime Images in urban zones


The generation of non saturated light intensity satellite images is problematic due to limitations in the sensor design. Saturated nighttime images make difficult to identify a single local maximum within a defined neighborhood.

Therefore, we propose a representation inspired on the Newton's Law of Gravitation to approximate the maximum values in saturated regions replacing the original luminance value by the sum $g_{i,j}$ defined in Equation \ref{gravitational}. We call it Gravitational Luminance Image Representation (GLIR), and it is denoted by the matrix $G$. The GLIR represents the total gravitational force exerted on a location with mass $m_i$ and it is calculated using the nighttime image $L$ as the gravitational field. Then, the following Equation is used to transform $L$ into $G$:


$$
    g_{i,j} = \sum_{x = i-h  }^{ i+h } \sum_{y = j-h}^{j+h} = \frac{m_i m_j}{d^2}
$$


where $m_1 = L_{i,j}, m_2 = L_{x,y} $, $d = \sqrt((x-i)^2 + (y-j)^2)$ is the distance between two {pixels}, and $h$ is a window size that constraints the computations in a neighborhood of size $(2h+1) \times (2h+1)$. This function produces a gravitational representation $G$, that reduces the saturation problem, while preserves the luminance local maxima in $L$ with the highest priority. Thus, it is used to determine the location of maximum priority levels located in saturated areas.

## Tutorial for using the method.

The ```Tutorial for light sensor locations.ipynb``` contains the steps to find the location of the most vulnerable urban regions with highest light pollution levels.

The main figures of the poster "optimal_sensor_location_poster.pdf" are produced with this software.

If you find this software useful please cite us:

```
@INPROCEEDINGS{lopezFarias2021b,
  author={Lopez-Farias, Rodrigo and Lamphar, Hector},
  booktitle={ALAN 2021, Artificial Light at Night}, 
  title={A methodology for a light pollution network with optimal sensor location}, 
  year={2021},
  page={73},
  note = {\url{https://artificiallightatnight.weebly.com/uploads/3/7/0/5/37053463/alan_2021_abstract_booklet__1_.pdf}}
  }
```


> Written with [StackEdit](https://stackedit.io/).